#!/usr/bin/env python3
"""
Package HyperBDR Best Practices Generator as a .skill file
"""

import os
import zipfile
import shutil
from pathlib import Path


def package_skill(skill_dir: str, output_dir: str):
    """Package skill directory into .skill file."""
    skill_path = Path(skill_dir)
    skill_name = skill_path.name
    
    # Create output directory if not exists
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Create .skill file (zip archive)
    skill_file = output_path / f"{skill_name}.skill"
    
    print(f"Packaging {skill_name} into {skill_file}...")
    
    with zipfile.ZipFile(skill_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through skill directory
        for root, dirs, files in os.walk(skill_path):
            for file in files:
                file_path = Path(root) / file
                
                # Skip .skill files and __pycache__
                if file.endswith('.skill') or '__pycache__' in str(file_path):
                    continue
                
                # Calculate relative path
                arcname = file_path.relative_to(skill_path)
                
                # Add to zip
                zipf.write(file_path, arcname)
                print(f"  Added: {arcname}")
    
    # Get file size
    file_size = skill_file.stat().st_size
    size_mb = file_size / (1024 * 1024)
    
    print(f"\n✓ Skill packaged successfully!")
    print(f"  File: {skill_file}")
    print(f"  Size: {file_size:,} bytes ({size_mb:.2f} MB)")
    
    return skill_file


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Package HyperBDR Best Practices Generator as .skill file'
    )
    parser.add_argument(
        '--skill-dir',
        default='skill-bestprodoc',
        help='Skill directory to package'
    )
    parser.add_argument(
        '--output-dir',
        default='.',
        help='Output directory for .skill file'
    )
    
    args = parser.parse_args()
    
    # Get script directory
    script_dir = Path(__file__).parent
    
    # Resolve paths
    skill_dir = script_dir / args.skill_dir
    output_dir = script_dir / args.output_dir
    
    # Verify skill directory exists
    if not skill_dir.exists():
        print(f"✗ Error: Skill directory not found: {skill_dir}")
        return 1
    
    # Verify SKILL.md exists
    skill_md = skill_dir / 'SKILL.md'
    if not skill_md.exists():
        print(f"✗ Error: SKILL.md not found in {skill_dir}")
        return 1
    
    # Package skill
    try:
        package_skill(str(skill_dir), str(output_dir))
        return 0
    except Exception as e:
        print(f"✗ Error packaging skill: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    exit(main())