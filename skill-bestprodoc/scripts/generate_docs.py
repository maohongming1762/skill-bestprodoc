#!/usr/bin/env python3
"""
HyperBDR Best Practices Documentation Generator

This script generates HyperBDR disaster recovery best practices documentation
in Chinese and English based on project data and template structure.
"""

import os
import re
import json
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional
import argparse


class ProjectDataParser:
    """Parse project data from Markdown files."""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.content = self._read_file()
        self.data = self._parse_content()
    
    def _read_file(self) -> str:
        """Read the project data file."""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def _parse_content(self) -> Dict[str, Any]:
        """Parse the Markdown content into structured data."""
        data = {
            'project_name': '',
            'customer': '',
            'industry': '',
            'business_characteristics': '',
            'key_systems': '',
            'scale': '',
            'source_environment': '',
            'target_environment': '',
            'dr_objectives': '',
            'challenges': [],
            'solutions': [],
            'benefits': [],
            'highlights': [],
            'architecture_image': None
        }
        
        # Extract project name from file path
        data['project_name'] = Path(self.file_path).stem
        
        # Parse sections
        sections = self._extract_sections()
        
        # Extract project background
        if '项目背景' in sections or 'Project Background' in sections:
            bg_section = sections.get('项目背景', sections.get('Project Background', ''))
            data.update(self._parse_background(bg_section))
        
        # Extract architecture
        if '架构图' in sections or 'Architecture Diagram' in sections:
            arch_section = sections.get('架构图', sections.get('Architecture Diagram', ''))
            data['architecture_image'] = self._extract_image(arch_section)
        
        # Extract challenges
        if '客户挑战' in sections or 'Customer Challenges' in sections:
            challenge_section = sections.get('客户挑战', sections.get('Customer Challenges', ''))
            data['challenges'] = self._parse_list_items(challenge_section)
        
        # Extract solutions
        if '解决方案' in sections or 'Solutions' in sections:
            solution_section = sections.get('解决方案', sections.get('Solutions', ''))
            data['solutions'] = self._parse_list_items(solution_section)
        
        # Extract benefits
        if '客户收益' in sections or 'Customer Benefits' in sections:
            benefit_section = sections.get('客户收益', sections.get('Customer Benefits', ''))
            data['benefits'] = self._parse_list_items(benefit_section)
        
        # Extract highlights
        if '项目亮点展示' in sections or 'Project Highlights' in sections:
            highlight_section = sections.get('项目亮点展示', sections.get('Project Highlights', ''))
            data['highlights'] = self._parse_list_items(highlight_section)
        
        return data
    
    def _extract_sections(self) -> Dict[str, str]:
        """Extract sections from Markdown content."""
        sections = {}
        current_section = 'header'
        current_content = []
        
        lines = self.content.split('\n')
        for line in lines:
            # Check for section headers
            if line.startswith('#'):
                if current_content:
                    sections[current_section] = '\n'.join(current_content).strip()
                current_section = line.lstrip('#').strip()
                current_content = []
            else:
                current_content.append(line)
        
        if current_content:
            sections[current_section] = '\n'.join(current_content).strip()
        
        return sections
    
    def _parse_background(self, content: str) -> Dict[str, str]:
        """Parse background section."""
        data = {}
        
        # Extract customer name
        customer_match = re.search(r'客户名称[:：]\s*(.+)', content[0:500] if len(content) > 500 else content)
        if customer_match:
            data['customer'] = customer_match.group(1).strip()
        
        # Extract migration requirements
        migration_match = re.search(r'迁移需求[:：]\s*(.+)', content)
        if migration_match:
            data['migration_requirements'] = migration_match.group(1).strip()
        
        # Extract business system types
        system_match = re.search(r'业务系统类型[:：]\s*(.+)', content)
        if system_match:
            data['business_characteristics'] = system_match.group(1).strip()
        
        # Extract scale information
        scale_matches = re.findall(r'\d+[\+]*\s*(虚拟机|VM|主机|TB|GB)', content)
        if scale_matches:
            data['scale'] = ', '.join(scale_matches)
        
        # Extract environment information
        env_matches = re.findall(r'(VMware|KVM|华为云|AWS|Azure|云平台)', content)
        if env_matches:
            data['source_environment'] = env_matches[0] if env_matches else ''
            if len(env_matches) > 1:
                data['target_environment'] = env_matches[-1]
        
        return data
    
    def _extract_image(self, content: str) -> Optional[str]:
        """Extract image reference from content."""
        image_match = re.search(r'!\[\]\((.+)\)', content)
        if image_match:
            return image_match.group(1).strip()
        return None
    
    def _parse_list_items(self, content: str) -> List[str]:
        """Parse list items from content."""
        items = []
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            if line.startswith('*') or line.startswith('-'):
                item = line.lstrip('*-').strip()
                if item:
                    items.append(item)
        
        return items


class TemplateProcessor:
    """Process templates and generate documentation."""
    
    def __init__(self, template_dir: str):
        self.template_dir = template_dir
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict[str, str]:
        """Load all template files."""
        templates = {}
        
        template_files = [
            'zh-concise-template.md',
            'en-concise-template.md',
            'zh-standard-template.md',
            'en-standard-template.md',
            'zh-complete-template.md',
            'en-complete-template.md'
        ]
        
        for template_file in template_files:
            template_path = os.path.join(self.template_dir, template_file)
            if os.path.exists(template_path):
                with open(template_path, 'r', encoding='utf-8') as f:
                    templates[template_file] = f.read()
        
        return templates
    
    def generate_document(self, template_name: str, project_data: Dict[str, Any]) -> str:
        """Generate documentation from template."""
        if template_name not in self.templates:
            raise ValueError(f"Template {template_name} not found")
        
        template = self.templates[template_name]
        
        # Replace placeholders with project data
        document = self._replace_placeholders(template, project_data)
        
        return document
    
    def _replace_placeholders(self, template: str, data: Dict[str, Any]) -> str:
        """Replace placeholders in template with actual data."""
        # Basic replacements
        replacements = {
            '[项目名称]': data.get('project_name', ''),
            '[Project Name]': data.get('project_name', ''),
            '[客户名称]': data.get('customer', ''),
            '[Customer Name]': data.get('customer', ''),
            '[行业描述]': data.get('industry', ''),
            '[Industry Description]': data.get('industry', ''),
            '[业务特点描述]': data.get('business_characteristics', ''),
            '[Business Characteristics]': data.get('business_characteristics', ''),
            '[关键系统列表]': data.get('key_systems', ''),
            '[Key Systems List]': data.get('key_systems', ''),
            '[主机数量]': data.get('scale', ''),
            '[Number of Hosts]': data.get('scale', ''),
            '[存储容量]': self._extract_storage(data.get('scale', '')),
            '[Storage Capacity]': self._extract_storage(data.get('scale', '')),
            '[源端平台]': data.get('source_environment', ''),
            '[Source Platform]': data.get('source_environment', ''),
            '[容灾目标和要求]': data.get('dr_objectives', ''),
            '[DR Objectives and Requirements]': data.get('dr_objectives', ''),
            '[场景描述]': '容灾场景',
            '[Scenario Description]': 'disaster recovery scenario'
        }
        
        # Replace core capabilities
        if data.get('solutions'):
            capabilities = data['solutions'][:3]  # Take first 3 solutions
            for i, cap in enumerate(capabilities, 1):
                replacements[f'[核心能力{i}]'] = cap
                replacements[f'[详细描述]'] = cap
                replacements[f'[Core Capability {i}]'] = cap
                replacements[f'[Detailed Description]'] = cap
        
        # Replace challenges
        if data.get('challenges'):
            challenges = data['challenges'][:4]  # Take first 4 challenges
            for i, challenge in enumerate(challenges, 1):
                replacements[f'[挑战{i}]'] = challenge
                replacements[ f'[挑战详细说明]'] = challenge
                replacements[f'[Challenge {i}]'] = challenge
                replacements[f'[Detailed Challenge Description]'] = challenge
                replacements[f'[解决方案详细说明]'] = 'HyperBDR提供相应解决方案'
                replacements[f'[Detailed Solution Description]'] = 'HyperBDR provides corresponding solutions'
        
        # Replace solutions
        if data.get('solutions'):
            solutions = data['solutions'][:4]
            for i, solution in enumerate(solutions, 1):
                replacements[f'[解决方案详细说明]'] = solution
                replacements[f'[Detailed Solution Description]'] = solution
        
        # Apply replacements
        document = template
        for placeholder, value in replacements.items():
            document = document.replace(placeholder, value)
        
        return document
    
    def _extract_storage(self, scale_text: str) -> str:
        """Extract storage information from scale text."""
        storage_match = re.search(r'(\d+[\+]*)\s*(TB|GB)', scale_text)
        if storage_match:
            return f"{storage_match.group(1)} {storage_match.group(2)}"
        return 'N/A'


class DocumentationGenerator:
    """Main documentation generator."""
    
    def __init__(self, project_data_dir: str, template_dir: str, output_dir: str):
        self.project_data_dir = project_data_dir
        self.template_dir = template_dir
        self.output_dir = output_dir
        self.template_processor = TemplateProcessor(template_dir)
    
    def generate(self, project_name: str) -> Dict[str, str]:
        """Generate all documentation for a project."""
        # Find project data file
        project_data_path = self._find_project_data(project_name)
        if not project_data_path:
            raise ValueError(f"Project data not found for {project_name}")
        
        # Parse project data
        parser = ProjectDataParser(project_data_path)
        project_data = parser.data
        
        # Create output directory
        output_path = os.path.join(self.output_dir, project_name)
        os.makedirs(output_path, exist_ok=True)
        
        # Copy images if they exist
        self._copy_images(project_data_path, output_path)
        
        # Generate documents
        generated_files = {}
        
        # Chinese documents
        for version in ['concise', 'standard', 'complete']:
            zh_template = f'zh-{version}-template.md'
            zh_filename = f"{project_name}最佳实践-{self._version_to_zh(version)}-中文.md"
            zh_content = self.template_processor.generate_document(zh_template, project_data)
            
            zh_file_path = os.path.join(output_path, zh_filename)
            with open(zh_file_path, 'w', encoding='utf-8') as f:
                f.write(zh_content)
            
            generated_files[zh_filename] = zh_file_path
            
            # English documents
            en_template = f'en-{version}-template.md'
            en_filename = f"{project_name}Best Practices-{self._version_to_en(version)}-English.md"
            en_content = self.template_processor.generate_document(en_template, project_data)
            
            en_file_path = os.path.join(output_path, en_filename)
            with open(en_file_path, 'w', encoding='utf-8') as f:
                f.write(en_content)
            
            generated_files[en_filename] = en_file_path
        
        return generated_files
    
    def _find_project_data(self, project_name: str) -> Optional[str]:
        """Find project data file."""
        # Search in project-data directory
        for root, dirs, files in os.walk(self.project_data_dir):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    if project_name in file or project_name in Path(file_path).parent.name:
                        return file_path
        return None
    
    def _copy_images(self, project_data_path: str, output_path: str):
        """Copy images from project data to output."""
        project_dir = Path(project_data_path).parent
        images_dir = os.path.join(project_dir, 'images')
        
        if os.path.exists(images_dir):
            output_images_dir = os.path.join(output_path, 'images')
            shutil.copytree(images_dir, output_images_dir, dirs_exist_ok=True)
    
    def _version_to_zh(self, version: str) -> str:
        """Convert version to Chinese."""
        version_map = {
            'concise': '简明',
            'standard': '标准',
            'complete': '完整'
        }
        return version_map.get(version, version)
    
    def _version_to_en(self, version: str) -> str:
        """Convert version to English."""
        version_map = {
            'concise': 'Concise',
            'standard': 'Standard',
            'complete': 'Complete'
        }
        return version_map.get(version, version.capitalize())


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate HyperBDR Best Practices Documentation'
    )
    parser.add_argument(
        'project_name',
        help='Name of the project (e.g., project-t-system)'
    )
    parser.add_argument(
        '--project-data-dir',
        default='project-data',
        help='Directory containing project data'
    )
    parser.add_argument(
        '--template-dir',
        default='assets/templates',
        help='Directory containing template files'
    )
    parser.add_argument(
        '--output-dir',
        default='output',
        help='Output directory for generated documents'
    )
    
    args = parser.parse_args()
    
    # Get script directory
    script_dir = Path(__file__).parent
    
    # Resolve paths
    project_data_dir = os.path.join(script_dir, args.project_data_dir)
    template_dir = os.path.join(script_dir, args.template_dir)
    output_dir = os.path.join(script_dir, args.output_dir)
    
    # Generate documentation
    generator = DocumentationGenerator(project_data_dir, template_dir, output_dir)
    
    try:
        generated_files = generator.generate(args.project_name)
        
        print("Documentation generated successfully!")
        print("\nGenerated files:")
        for filename, filepath in generated_files.items():
            print(f"  - {filename}: {filepath}")
        
    except Exception as e:
        print(f"Error generating documentation: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())