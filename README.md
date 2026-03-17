# HyperBDR Best Practices Documentation Generator

A skill for generating HyperBDR disaster recovery best practices documentation in Chinese and English based on project data.

## Overview

This skill generates comprehensive HyperBDR disaster recovery best practices documentation based on project data and template structure. It produces bilingual (Chinese/English) Markdown documentation in three versions:

- **Concise Version**: Quick reference guide with key points and steps
- **Standard Version**: Detailed implementation guide with explanations
- **Complete Version**: Full documentation with all details, examples, and troubleshooting

## Usage

### Basic Usage

When the user requests HyperBDR best practices documentation generation:

1. Identify the project data directory
2. Read the project data file
3. Generate three versions (concise, standard, complete)
4. Output bilingual documentation (Chinese and English)
5. Provide summary of generated files

### Example Prompts

- "根据project-data/project-t-system生成最佳实践文档"
- "auto最佳实践 for T-System项目"
- "Generate HyperBDR best practices documentation from project data"
- "Create bilingual best practices documentation for the Mexico migration project"

## Input Requirements

### Project Data Structure

```
project-data/
└── [projectName]/
    ├── project-info.md          # Project data file in Markdown format
    └── images/                  # Architecture diagrams and images
```

### Project Data Format

The project data file should contain the following sections:

1. **Project Background** (项目背景)
   - Customer name and background
   - Migration requirements
   - Business system types
   - Host specifications
   - Backup strategies

2. **Architecture Diagram** (架构图)
   - Visual representation of the architecture
   - Image references in `images/` directory

3. **Customer Challenges** (客户挑战)
   - Specific pain points and difficulties
   - Technical constraints
   - Business requirements

4. **Solutions** (解决方案)
   - HyperBDR capabilities used
   - Implementation approaches
   - Technical advantages

5. **Customer Benefits** (客户收益)
   - Business value delivered
   - Operational improvements
   - Cost savings

6. **Project Highlights** (项目亮点展示)
   - Key achievements
   - Innovation points
   - Success metrics

## Output Format

The skill generates documentation in the following structure:

```
output/
└── [projectName]/
    ├── [projectName]最佳实践-简明-中文.md
    ├── [projectName]Best Practices-Concise-English.md
    ├── [projectName]最佳实践-标准-中文.md
    ├── [projectName]Best Practices-Standard-English.md
    ├── [projectName]最佳实践-完整-中文.md
    ├── [projectName]Best Practices-Complete-English.md
    └── images/                  # Copied from project data
```

## Document Structure

Each generated document follows this structure:

### 1. Project Overview (项目概述)
- Customer and scenario details
- Business characteristics
- System scale
- Source/target environments
- DR objectives

### 2. Business Challenges & HyperBDR Solutions (业务挑战与HyperBDR解决方案)
- System complexity
- RPO/RTO requirements
- Target environment costs
- Bandwidth and synchronization
- Deployment and operational complexity

### 3. HyperBDR Solution & Architecture (HyperBDR方案与架构)
- Overall approach
- Architecture key points
- HyperBDR core capabilities

### 4. Implementation & DR Drill Best Practices (实施要点与演练最佳实践)
- Data replication phase
- DR drill and takeover phase
- Best practices and recommendations

### 5. Key Results & Metrics (关键成果与指标)
- Performance metrics
- RTO/RPO achievements
- Cost optimization results

### 6. Project Summary (项目总结)
- Key achievements
- Project value
- Typical scenarios

## Using the Generator Script

The skill includes a Python script for generating documentation:

```bash
python scripts/generate_docs.py project-name
```

### Options

- `--project-data-dir`: Directory containing project data (default: project-data)
- `--template-dir`: Directory containing template files (default: assets/templates)
- `--output-dir`: Output directory for generated documents (default: output)

### Example

```bash
python scripts/generate_docs.py project-t-system \
  --project-data-dir ../project-data \
  --output-dir ../output
```

## HyperBDR Knowledge Integration

The skill integrates knowledge from https://docs.oneprocloud.com/ covering:

### Network Planning
- Migration & DR network planning
- SaaS network communication
- AWS cross-region DR

### Policy Management
- Policy best practices
- Pre & post scripts
- Strategy-based synchronization

### Orchestration
- HyperBDR orchestration best practices
- Boot in Cloud one-click recovery
- Parallel recovery and dependency management

### VMware Agentless Migration
- VMware agentless migration
- Automated driver adaptation
- Batch host migration

### Object Storage Technology
- Boot in Cloud with object storage
- Cost optimization
- Elastic cloud capabilities

### Failback Operations
- Cloud failback to VMware
- DR failback best practices

## Error Best

### Common Issues and Solutions

1. **Missing Project Data**
   - Error: Project data file not found
`   - Solution: Verify project-data directory structure

2. **Invalid Markdown Format**
   - Error: Cannot parse project data
   - Solution: Check Markdown syntax and structure

3. **Missing Required Sections**
   - Error: Required sections not found
   - Solution: Ensure project data contains all required sections

4. **Image Reference Errors**
   - Error: Cannot find referenced images
   - Solution: Verify images directory and file names

5. **Translation Errors**
   - Error: Cannot translate to English
   - Solution: Check for unsupported characters or formatting

## Best Practices

### For Project Data
- Use consistent Markdown formatting
- Include all required sections
- Provide clear architecture diagrams
- Use specific metrics and data

### For Generated Documentation
- Maintain consistent structure across versions
- Ensure accurate technical terminology
- Include relevant HyperBDR capabilities
- Provide actionable recommendations

### For Quality Assurance
- Verify Chinese-English correspondence
- Check all links and references
- Validate Markdown formatting
- Test document rendering

## Testing

The skill includes test cases in `evals/evals.json`. To run tests:

```bash
python -m pytest tests/
```

## References

- HyperBDR Documentation: https://docs.oneprocloud.com/
- Technical Practices: https://docs.oneprocloud.com/userguide/technical-practices/
- Project Practices: https://docs.oneprocloud.com/userguide/project-practices/
- HyperBDR Manual: https://docs.oneprocloud.com/userguide/dr/

## License

This skill is part of the HyperBDR ecosystem and follows the same licensing terms.