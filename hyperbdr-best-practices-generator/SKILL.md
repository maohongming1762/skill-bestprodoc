---
name: hyperbdr-best-practices-generator
description: Generate HyperBDR disaster recovery best practices documentation in Chinese and English based on project data. Use this skill whenever the user mentions "auto最佳实践", "最佳实践文档", "best practices", or needs to create HyperBDR DR documentation from project data. This skill automatically generates bilingual (Chinese/English) Markdown documentation in three versions: concise, standard, and complete, following best practices standards from https://docs.oneprocloud.com/.
---

# HyperBDR Best Practices Documentation Generator

## Overview

This skill generates comprehensive HyperBDR disaster recovery best practices documentation based on project data and template structure. It produces bilingual (Chinese/English) Markdown documentation in three versions:

- **Concise Version**: Quick reference guide with key points and steps
- **Standard Version**: Detailed implementation guide with explanations  
- **Complete Version**: Full documentation with all details, examples, and troubleshooting

## When to Use

Use this skill when the user:
- Mentions "auto最佳实践" or "最佳实践文档"
- Requests generation of best practices documentation
- Needs to create HyperBDR DR documentation
- Asks for bilingual (Chinese/English) documentation
- Wants to convert project data into best practices format

## Required Actions

### Step 1: Locate Project Data

Find the project data file in the `project-data/` directory. The structure should be:

```
project-data/
└── [project-name]/
    ├── project-info.md          # Project data in Markdown
    └── images/                  # Architecture diagrams
```

### Step 2: Read and Parse Project Data

Read the project data Markdown file and extract:
- Project background (customer name, industry, business characteristics)
- Architecture diagram references
- Customer challenges
- HyperBDR solutions
- Customer benefits
- Project highlights

### Step 3: Extract Key Information

Extract the following from project data:
- Customer name and background
- Migration requirements
- Business system types
- System scale (number of VMs, storage capacity)
- Source and target environments
- RPO/RTO requirements
- HyperBDR capabilities used

### Step 4: Generate Documentation

Generate 6 documents (3 versions × 2 languages):

#### For Each Version (Concise, Standard, Complete):

**Chinese Documents:**
1. `[项目名称]最佳实践-简明-中文.md`
2. `[项目名称]最佳实践-标准-中文.md`
3. `[项目名称]最佳实践-完整-中文.md`

**English Documents:**
1. `[项目名称]Best Practices-Concise-English.md`
2. `[项目名称]Best Practices-Standard-English.md`
3. `[项目名称]Best Practices-Complete-English.md`

### Step 5: Document Structure

Each document MUST include these 6 main sections:

#### 1. Project Overview (项目概述)
- Customer and scenario details in table format
- Business characteristics
- System scale (number of hosts, storage)
- Source/target environments
- DR objectives
- HyperBDR core value (for standard/complete versions)

#### 2. Business Challenges & HyperBDR Solutions (业务挑战与HyperBDR解决方案)
- Table format with 3 columns: Challenge, Description, HyperBDR Solution
- Extract challenges from project data
- Map challenges to HyperBDR capabilities
- For standard/complete versions, include detailed analysis

#### 3. HyperBDR Solution & Architecture (HyperBDR方案与架构)
- Overall approach description
- Architecture key points:
  - Production environment details
  - DR environment details
  - Storage layer configuration
  - Replication strategy
- Architecture diagram (reference from project data)
- Table showing HyperBDR core capabilities with application and value

#### 4. Implementation & DR Drill Best Practices (实施要点与演练最佳实践)
- **Concise**: Brief summary of data replication and drill phases
- **Standard**: Detailed steps with tables for each phase
- **Complete**: Comprehensive implementation guide with:
  - Pre-implementation preparation
  - Data replication phase details
  - Drill and takeover phase with step-by-step tables
  - Post-drill processing

#### 5. Key Results & Metrics (关键成果与指标)
- Performance metrics (RTO, RTO, data transfer rates)
- Cost metrics
- Operational metrics
- HyperBDR contributions

#### 6. Project Summary (项目总结)
- Key achievements
- Project value
- Typical scenarios
- For complete version: Lessons learned and future outlook

### Step 6: Version-Specific Content

#### Concise Version
- Focus on key points and tables
- Brief descriptions (1-2 sentences)
- Essential metrics only
- Quick reference format

#### Standard Version
- Detailed explanations (2-3 sentences)
- Step-by-step guidance
- Comprehensive tables
- Practical examples

#### Complete Version
- All details from standard version
- Additional troubleshooting section
- Security and compliance section
- Reference resources section
- Appendices (glossary, configuration checklist, contacts, version history)

### Step 7: Apply HyperBDR Knowledge

Integrate knowledge from https://docs.oneprocloud.com/:

#### Core Capabilities to Include:
- **Boot in Cloud (云端启动)**: Object storage as intermediate layer, one-click recovery
- **Orchestration (编排)**: Unified scheduling, dependency management, parallel recovery
- **VMware Agentless Migration (VMware无代理)**: No agent installation, direct VMware API access
- **Automated Driver Adaptation (自动化驱动适配)**: Automatic driver injection and loading
- **Policy-Based Synchronization (策略化同步)**: Flexible sync strategies based on RPO requirements
- **Batch Migration (批量迁移)**: Batch processing for large-scale migrations

#### Network Planning:
- Migration & DR network planning
- SaaS network communication requirements
- Cross-region DR considerations

#### Orchestration Best Practices:
- Recovery sequencing (database first, then applications)
- Dependency management
- Parallel recovery strategies
- Boot in Cloud one-click recovery

### Step 8: English Translation

For English versions:
- Translate all Chinese content accurately
- Maintain consistent structure with Chinese versions
- Use professional technical terminology
- Ensure technical accuracy
- Reference translation guide in `references/translation-guide.md`

### Step 9: Save Documents

Save all generated documents to an `output/` directory:
```
output/
└── [project-name]/
    ├── [project-name]最佳实践-简明-中文.md
    ├── [project-name]Best Practices-Concise-English.md
    ├── [project-name]最佳实践-标准-中文.md
    ├── [project-name]Best Practices-Standard-English.md
    ├── [project-name]最佳实践-完整-中文.md
    ├── [project-name]Best Practices-Complete-English.md
    └── images/              # Copy from project data
```

### Step 10: Provide Summary

After generating documents, provide a summary:
- List all generated files with paths
- Highlight key information extracted from project data
- Note any issues or assumptions made
- Suggest next steps (review, edit, distribute)

## Templates and References

### Template Files
Use templates in `assets/templates/`:
- `zh-concise-template.md`
- `en-concise-template.md`
- `zh-standard-template.md`
- `en-standard-template.md`
- `zh-complete-template.md`
- `en-complete-template.md`

### Reference Files
- `references/hyperbdr-knowledge.md`: Comprehensive HyperBDR knowledge base
- `references/translation-guide.md`: Chinese-English terminology and translation guide

## Quality Checklist

Before completing, ensure:

- [ ] All 6 documents are generated
- [ ] Each document has all 6 main sections
- [ ] Chinese and English versions correspond accurately
- [ ] HyperBDR capabilities are correctly integrated
- [ ] Key project information is extracted and included
- [ ] Architecture diagrams are referenced correctly
- [ ] Tables are properly formatted
- [ ] Markdown syntax is correct
- [ ] Technical terminology is accurate
- [ ] Version-specific content is appropriate

## Error Handling

### Common Issues:

1. **Missing Project Data**
   - Check `project-data/` directory structure
   - Verify project data file exists
   - Ensure file is in Markdown format

2. **Missing Required Sections**
   - Check if project data has all required sections
   - Inform user if sections are missing
   - Make reasonable assumptions if possible

3. **Image References**
   - Copy images from project data to output
   - Verify image paths are correct
   - Note if images are missing

4. **Translation Issues**
   - Use terminology from translation guide
   - Maintain technical accuracy
   - Ensure proper grammar and phrasing

## Examples

### Example 1: Basic Generation
```
User: 根据project-data/project-t-system生成最佳实践文档
Action: 
1. Read project data from project-data/project-t-system/
2. Extract key information (T-System, 3500+ VMs, VMware to HCS8.2)
3. Generate 6 documents with proper structure
4. Save to output/project-t-system/
5. Provide summary of generated files
```

### Example 2: With Specific Focus
```
User: Generate HyperBDR best practices for SAP HANA DR project, focus on orchestration
Action:
1. Generate standard and complete versions with emphasis on orchestration
2. Include detailed orchestration configuration
3. Highlight orchestration-driven takeover process
4. Provide examples of orchestration workflows
```

## Notes

- This skill focuses on HyperBDR architecture and capabilities
- Three versions serve different use cases (quick reference, implementation guide, comprehensive documentation)
- Bilingual documentation supports global teams
- Always verify extracted information matches project data
- Use HyperBDR knowledge from documentation website
- Follow best practices from https://docs.oneprocloud.com/