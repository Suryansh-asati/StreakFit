#!/usr/bin/env python3
"""
StreakFit Dead Code and Unused File Detector

This script analyzes the StreakFit repository to detect:
1. Unused CSS files
2. Missing image references
3. Dead links in HTML
4. Unused image files
5. Duplicate/conflicting files
6. Unused CSS selectors (basic detection)
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from urllib.parse import urlparse

class DeadCodeDetector:
    def __init__(self, root_dir="."):
        self.root_dir = Path(root_dir)
        self.html_files = []
        self.css_files = []
        self.js_files = []
        self.image_files = []
        self.all_files = []
        
        # Track references
        self.css_references = defaultdict(list)
        self.js_references = defaultdict(list)
        self.image_references = defaultdict(list)
        self.html_links = defaultdict(list)
        
        # Issues found
        self.issues = {
            'missing_files': [],
            'unused_files': [],
            'dead_links': [],
            'duplicate_files': [],
            'inconsistent_paths': [],
            'unused_css_rules': []
        }
        
    def scan_files(self):
        """Scan directory for all relevant files."""
        print("📁 Scanning files...")
        
        for file_path in self.root_dir.rglob("*"):
            if file_path.is_file() and not any(part.startswith('.') for part in file_path.parts):
                self.all_files.append(file_path)
                
                if file_path.suffix.lower() == '.html':
                    self.html_files.append(file_path)
                elif file_path.suffix.lower() == '.css':
                    self.css_files.append(file_path)
                elif file_path.suffix.lower() == '.js':
                    self.js_files.append(file_path)
                elif file_path.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp']:
                    self.image_files.append(file_path)
        
        print(f"Found: {len(self.html_files)} HTML, {len(self.css_files)} CSS, {len(self.js_files)} JS, {len(self.image_files)} images")
    
    def analyze_html_references(self):
        """Analyze all references in HTML files."""
        print("🔍 Analyzing HTML references...")
        
        for html_file in self.html_files:
            try:
                content = html_file.read_text(encoding='utf-8')
                rel_path = html_file.relative_to(self.root_dir)
                
                # Find CSS references
                css_patterns = [
                    r'<link[^>]*href=["\'](.*?\.css)["\'][^>]*>',
                    r'<link[^>]*rel=["\']stylesheet["\'][^>]*href=["\'](.*?)["\'][^>]*>'
                ]
                
                for pattern in css_patterns:
                    for match in re.finditer(pattern, content, re.IGNORECASE):
                        css_ref = match.group(1)
                        if not css_ref.startswith('http'):
                            self.css_references[css_ref].append(str(rel_path))
                
                # Find JS references
                js_pattern = r'<script[^>]*src=["\'](.*?\.js)["\'][^>]*>'
                for match in re.finditer(js_pattern, content, re.IGNORECASE):
                    js_ref = match.group(1)
                    if not js_ref.startswith('http'):
                        self.js_references[js_ref].append(str(rel_path))
                
                # Find image references
                img_patterns = [
                    r'<img[^>]*src=["\'](.*?)["\'][^>]*>',
                    r'<link[^>]*href=["\'](.*?\.(?:png|jpg|jpeg|gif|svg|webp))["\'][^>]*>'
                ]
                
                for pattern in img_patterns:
                    for match in re.finditer(pattern, content, re.IGNORECASE):
                        img_ref = match.group(1)
                        if not img_ref.startswith('http') and '.' in img_ref:
                            self.image_references[img_ref].append(str(rel_path))
                
                # Find HTML links
                link_pattern = r'<a[^>]*href=["\'](.*?)["\'][^>]*>'
                for match in re.finditer(link_pattern, content, re.IGNORECASE):
                    link_ref = match.group(1)
                    if not link_ref.startswith('http') and not link_ref.startswith('mailto:') and not link_ref.startswith('#'):
                        self.html_links[link_ref].append(str(rel_path))
                        
            except Exception as e:
                print(f"Error reading {html_file}: {e}")
    
    def check_missing_files(self):
        """Check for missing referenced files."""
        print("❌ Checking for missing files...")
        
        # Check CSS files
        for css_ref, referencing_files in self.css_references.items():
            if not self._file_exists(css_ref):
                self.issues['missing_files'].append({
                    'type': 'CSS',
                    'file': css_ref,
                    'referenced_by': referencing_files
                })
        
        # Check JS files
        for js_ref, referencing_files in self.js_references.items():
            if not self._file_exists(js_ref):
                self.issues['missing_files'].append({
                    'type': 'JavaScript',
                    'file': js_ref,
                    'referenced_by': referencing_files
                })
        
        # Check image files
        for img_ref, referencing_files in self.image_references.items():
            if not self._file_exists(img_ref):
                self.issues['missing_files'].append({
                    'type': 'Image',
                    'file': img_ref,
                    'referenced_by': referencing_files
                })
        
        # Check HTML links
        for link_ref, referencing_files in self.html_links.items():
            if link_ref.endswith('.html') and not self._file_exists(link_ref):
                self.issues['dead_links'].append({
                    'link': link_ref,
                    'referenced_by': referencing_files
                })
    
    def check_unused_files(self):
        """Check for unused files."""
        print("🗑️ Checking for unused files...")
        
        # Get all referenced files
        all_refs = set()
        
        # Normalize paths and add references
        for refs in self.css_references.keys():
            all_refs.add(self._normalize_path(refs))
        for refs in self.js_references.keys():
            all_refs.add(self._normalize_path(refs))
        for refs in self.image_references.keys():
            all_refs.add(self._normalize_path(refs))
        
        # Check CSS files
        for css_file in self.css_files:
            rel_path = css_file.relative_to(self.root_dir)
            if not self._is_file_referenced(str(rel_path), all_refs):
                self.issues['unused_files'].append({
                    'type': 'CSS',
                    'file': str(rel_path),
                    'size': css_file.stat().st_size
                })
        
        # Check image files
        for img_file in self.image_files:
            rel_path = img_file.relative_to(self.root_dir)
            if not self._is_file_referenced(str(rel_path), all_refs):
                self.issues['unused_files'].append({
                    'type': 'Image',
                    'file': str(rel_path),
                    'size': img_file.stat().st_size
                })
    
    def check_duplicate_files(self):
        """Check for duplicate or conflicting files."""
        print("👥 Checking for duplicate/conflicting files...")
        
        # Check for multiple HTML files that might serve same purpose
        html_names = [f.name for f in self.html_files]
        if 'index.html' in html_names and 'main.html' in [f.name for f in self.all_files]:
            self.issues['duplicate_files'].append({
                'type': 'HTML',
                'files': ['index.html', 'assets/main.html'],
                'issue': 'Multiple main pages detected'
            })
        
        # Check for conflicting CSS files
        css_names = [f.name for f in self.css_files]
        if 'styles.css' in css_names and 'main.css' in css_names:
            self.issues['duplicate_files'].append({
                'type': 'CSS',
                'files': ['assets/styles.css', 'assets/main.css'],
                'issue': 'Multiple main stylesheets with different usage patterns'
            })
    
    def check_path_inconsistencies(self):
        """Check for path inconsistencies."""
        print("🔧 Checking path inconsistencies...")
        
        # Check for mixed absolute/relative paths
        for css_ref, referencing_files in self.css_references.items():
            if css_ref.startswith('/'):
                for ref_file in referencing_files:
                    self.issues['inconsistent_paths'].append({
                        'type': 'CSS',
                        'file': css_ref,
                        'referenced_by': ref_file,
                        'issue': 'Uses absolute path'
                    })
    
    def analyze_css_usage(self):
        """Basic analysis of CSS usage."""
        print("🎨 Analyzing CSS usage...")
        
        for css_file in self.css_files:
            try:
                content = css_file.read_text(encoding='utf-8')
                
                # Extract CSS selectors (basic)
                selectors = re.findall(r'([.#][a-zA-Z_-][a-zA-Z0-9_-]*)', content)
                
                # Check if selectors are used in HTML
                unused_selectors = []
                for selector in set(selectors):
                    if not self._selector_used_in_html(selector):
                        unused_selectors.append(selector)
                
                if unused_selectors and len(unused_selectors) > 5:  # Only report if many unused
                    self.issues['unused_css_rules'].append({
                        'file': str(css_file.relative_to(self.root_dir)),
                        'unused_count': len(unused_selectors),
                        'sample_unused': unused_selectors[:10]
                    })
                    
            except Exception as e:
                print(f"Error analyzing CSS {css_file}: {e}")
    
    def _file_exists(self, ref_path):
        """Check if a referenced file exists."""
        # Try multiple path variations
        variations = [
            ref_path,
            ref_path.lstrip('/'),
            f"assets/{ref_path.lstrip('/')}",
            f"./{ref_path.lstrip('/')}"
        ]
        
        for variation in variations:
            full_path = self.root_dir / variation
            if full_path.exists():
                return True
        return False
    
    def _normalize_path(self, path):
        """Normalize a path for comparison."""
        return path.lstrip('/').replace('\\', '/')
    
    def _is_file_referenced(self, file_path, all_refs):
        """Check if a file is referenced."""
        normalized = self._normalize_path(file_path)
        
        # Check exact matches and variations
        for ref in all_refs:
            if normalized in ref or ref in normalized:
                return True
            if Path(normalized).name == Path(ref).name:
                return True
        return False
    
    def _selector_used_in_html(self, selector):
        """Check if a CSS selector is used in HTML (basic check)."""
        # Remove the . or # prefix
        class_or_id = selector[1:]
        
        for html_file in self.html_files:
            try:
                content = html_file.read_text(encoding='utf-8')
                if selector.startswith('.'):
                    # Check for class usage
                    if f'class="{class_or_id}"' in content or f"class='{class_or_id}'" in content:
                        return True
                    if f'class=".*{class_or_id}.*"' in content:
                        return True
                elif selector.startswith('#'):
                    # Check for id usage
                    if f'id="{class_or_id}"' in content or f"id='{class_or_id}'" in content:
                        return True
            except Exception:
                continue
        return False
    
    def generate_report(self):
        """Generate a comprehensive report."""
        print("\n" + "="*60)
        print("📊 STREAKFIT DEAD CODE ANALYSIS REPORT")
        print("="*60)
        
        total_issues = sum(len(issues) for issues in self.issues.values())
        print(f"\n🎯 SUMMARY: Found {total_issues} issues\n")
        
        # Missing files
        if self.issues['missing_files']:
            print("❌ MISSING FILES:")
            for item in self.issues['missing_files']:
                print(f"  • {item['type']}: {item['file']}")
                print(f"    Referenced by: {', '.join(item['referenced_by'])}")
            print()
        
        # Unused files
        if self.issues['unused_files']:
            print("🗑️ UNUSED FILES:")
            total_size = 0
            for item in self.issues['unused_files']:
                total_size += item['size']
                size_kb = item['size'] / 1024
                print(f"  • {item['type']}: {item['file']} ({size_kb:.1f} KB)")
            print(f"  Total wasted space: {total_size/1024:.1f} KB\n")
        
        # Dead links
        if self.issues['dead_links']:
            print("🔗 DEAD LINKS:")
            for item in self.issues['dead_links']:
                print(f"  • {item['link']}")
                print(f"    Referenced by: {', '.join(item['referenced_by'])}")
            print()
        
        # Duplicate files
        if self.issues['duplicate_files']:
            print("👥 DUPLICATE/CONFLICTING FILES:")
            for item in self.issues['duplicate_files']:
                print(f"  • {item['type']}: {item['issue']}")
                print(f"    Files: {', '.join(item['files'])}")
            print()
        
        # Path inconsistencies
        if self.issues['inconsistent_paths']:
            print("🔧 PATH INCONSISTENCIES:")
            for item in self.issues['inconsistent_paths']:
                print(f"  • {item['file']} ({item['issue']})")
                print(f"    In: {item['referenced_by']}")
            print()
        
        # Unused CSS rules
        if self.issues['unused_css_rules']:
            print("🎨 POTENTIALLY UNUSED CSS:")
            for item in self.issues['unused_css_rules']:
                print(f"  • {item['file']}: {item['unused_count']} unused selectors")
                print(f"    Sample: {', '.join(item['sample_unused'][:5])}")
            print()
        
        # Recommendations
        print("💡 RECOMMENDATIONS:")
        print("  1. Remove unused files to reduce repository size")
        print("  2. Fix missing file references or remove dead links")
        print("  3. Consolidate duplicate functionality")
        print("  4. Standardize path references (use relative paths)")
        print("  5. Clean up unused CSS rules")
        
        return self.issues
    
    def generate_cleanup_script(self):
        """Generate a script to clean up identified issues."""
        script_content = "#!/bin/bash\n"
        script_content += "# StreakFit Cleanup Script\n"
        script_content += "# Generated by dead_code_detector.py\n\n"
        script_content += "echo 'Starting StreakFit cleanup...'\n\n"
        
        # Remove unused files
        if self.issues['unused_files']:
            script_content += "# Remove unused files\n"
            for item in self.issues['unused_files']:
                script_content += f"echo 'Removing unused {item['type']}: {item['file']}'\n"
                script_content += f"# rm '{item['file']}'  # Uncomment to execute\n"
            script_content += "\n"
        
        script_content += "echo 'Cleanup complete!'\n"
        
        with open(self.root_dir / "cleanup_script.sh", "w") as f:
            f.write(script_content)
        
        print(f"📝 Generated cleanup script: cleanup_script.sh")
    
    def run_analysis(self):
        """Run complete analysis."""
        self.scan_files()
        self.analyze_html_references()
        self.check_missing_files()
        self.check_unused_files()
        self.check_duplicate_files()
        self.check_path_inconsistencies()
        self.analyze_css_usage()
        
        issues = self.generate_report()
        self.generate_cleanup_script()
        
        return issues

if __name__ == "__main__":
    detector = DeadCodeDetector()
    issues = detector.run_analysis()
    
    # Save detailed report
    with open("dead_code_report.json", "w") as f:
        json.dump(issues, f, indent=2)
    
    print(f"\n📄 Detailed report saved to: dead_code_report.json")