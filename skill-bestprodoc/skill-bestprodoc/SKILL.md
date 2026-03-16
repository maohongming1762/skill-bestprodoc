---
name: skill-bestprodoc
description: Generate HyperBDR disaster recovery best practices documentation in Chinese and English based on project data. Use this skill whenever the user mentions "auto最佳实践", "最佳实践文档", "best practices", or needs to create HyperBDR DR documentation from project data. This skill automatically generates bilingual (Chinese/English) Markdown documentation in standard version only, strictly following template structure.
---

# HyperBDR Best Practices Documentation Generator

## Overview

This skill generates comprehensive HyperBDR disaster recovery best practices documentation based on project data and template structure. It produces bilingual (Chinese/English) Markdown documentation in standard version only:

- **Standard Version**: Detailed implementation guide with explanations and best practices

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
    ├── project-info.md          # Project data in Markdown format only
    └── images/                  # Architecture diagrams
```

**IMPORTANT**: The project data file MUST be in `.md` format. If the file is not in `.md` format, display an error message and exit immediately.

### Step 2: Read and Parse Project Data

**Format Validation**: Before proceeding, verify that the project data file is in `.md` format.

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

Generate 2 documents (Chinese + English standard version):

**Chinese Document:**
1. `[项目名称]最佳实践-标准-中文.md`

**English Document:**
2. `[项目名称]Best Practices-Standard-English.md`

### Step 5: Document Structure

**CRITICAL**: Strictly preserve the template structure. Only H4+ headings and content can be modified/extended. H1, H2, and H3 headings must remain exactly as defined in the template.

Each document MUST include these 6 main sections (H1 level):

#### 1. Project Overview (项目概述) - H1
- Customer and scenario details in table format
- Business characteristics
- System scale (number of hosts, storage)
- Source/target environments
- DR objectives
- HyperBDR core value

#### 2. Business Challenges & HyperBDR Solutions (业务挑战与HyperBDR解决方案) - H1
- Table format with 3 columns: Challenge, Description, HyperBDR Solution
- Extract challenges from project data
- Map challenges to HyperBDR capabilities
- Include detailed analysis

#### 3. HyperBDR Solution & Architecture (HyperBDR方案与架构) - H1
- Overall approach description
- Architecture key points:
  - Production environment details
  - DR environment details
  - Storage layer configuration
  - Replication strategy
- Architecture diagram (reference from project data)
- Table showing HyperBDR core capabilities with application and value

#### 4. Implementation & DR Drill Best Practices (实施要点与演练最佳实践) - H1
- Detailed steps with tables for each phase
- Step-by-step guidance
- Comprehensive tables
- Practical examples

#### 5. Key Results & Metrics (关键成果与指标) - H1
- Performance metrics (RPO, RTO, data transfer rates)
- Cost metrics
- Operational metrics
- HyperBDR contributions

#### 6. Project Summary (项目总结) - H1
- Key achievements
- Project value
- Typical scenarios

### Step 6: Standard Version Content Guidelines

#### Standard Version Requirements
- Detailed explanations (2-3 sentences)
- Step-by-step guidance
- Comprehensive tables
- Practical examples
- Strictly follow template structure (H1-H3 headings cannot be modified)
- Only H4+ headings and content can be extended

### Step 7: Apply HyperBDR Knowledge

Use local reference files and technical documentation:

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

**IMPORTANT**: 
- Technical reference: Use https://docs.oneprocloud.com/ for HyperBDR technical knowledge and best practices
- Non-technical content: ONLY use project data source, do NOT fetch from network
- All project-specific information must come from the provided project data file

### Step 8: Data Calculations

**IMPORTANT**: For any data calculations required in the documentation (e.g., RPO/RTO metrics, storage capacity calculations, data transfer rates), ensure accuracy by:

- Using appropriate calculation tools or utilities for numerical computations
- Verifying all calculated values against project data
- Ensuring units and formats are consistent
- Documenting calculation methods where appropriate
- Calculation tools can be customized based on specific requirements

### Step 9: English Translation

For English versions:
- Translate all Chinese content accurately
- Maintain consistent structure with Chinese versions
- Use professional technical terminology
- Ensure technical accuracy
- Reference translation guide in `references/translation-guide.md`

### Step 10: Save Documents

Save all generated documents to an `output/` directory:
```
output/
└── [project-name]/
    ├── [项目名称]最佳实践-标准-中文.md
    ├── [项目名称]Best Practices-Standard-English.md
    └── images/              # Copy from project data
```

### Step 11: Provide Summary

After generating documents, provide a summary:
- List all generated files with paths
- Highlight key information extracted from project data
- Note any issues or assumptions made
- Suggest next steps (review, edit, distribute)

## Templates and References

### Template Files
Use templates in `assets/templates/`:
- `zh-standard-template.md` - Chinese standard template
- `en-standard-template.md` - English standard template

**IMPORTANT**: These templates define the fixed structure. Only H4+ headings and content can be modified. H1, H2, and H3 headings must remain exactly as defined.

### Reference Files
- `references/hyperbdr-knowledge.md`: Comprehensive HyperBDR knowledge base
- `references/translation-guide.md`: Chinese-English terminology and translation guide

## Quality Checklist

Before completing, ensure:

- [ ] Project data file is in `.md` format
- [ ] Both documents (Chinese + English) are generated
- [ ] Each document has all 6 main sections (H1 headings)
- [ ] H1, H2, and H3 headings match template exactly
- [ ] Only H4+ headings have been modified/extended
- [ ] Chinese and English versions correspond accurately
- [ ] HyperBDR capabilities are correctly integrated
- [ ] Key project information is extracted and included
- [ ] Architecture diagrams are referenced correctly
- [ ] Tables are properly formatted
- [ ] Markdown syntax is correct
- [ ] Technical terminology is accurate
- [ ] All numerical calculations are accurate and validated
- [ ] No online/network resources were used

## Error Handling

### Common Issues:

1. **Invalid File Format**
   - **Check**: Verify project data file extension is `.md`
   - **Action**: If file is not `.md` format, display error message: "项目数据源格式必须为md格式。当前文件格式不支持，请将数据源转换为.md格式后重试。" and exit immediately
   - **Supported formats**: Only `.md` files are accepted

2. **Missing Project Data**
   - Check `project-data/` directory structure
   - Verify project data file exists
   - Ensure file is in Markdown format

3. **Missing Required Sections**
   - Check if project data has all required sections
   - Inform user if sections are missing
   - Make reasonable assumptions if possible

4. **Image References**
   - Copy images from project data to output
   - Verify image paths are correct
   - Note if images are missing

5. **Translation Issues**
   - Use terminology from translation guide
   - Maintain technical accuracy
   - Ensure proper grammar and phrasing

6. **Calculation Errors**
   - Verify all numerical calculations
   - Use appropriate calculation tools for complex computations
   - Document calculation methods for transparency

7. **Data Source Issues**
   - Technical content: Use https://docs.oneprocloud.com/ for HyperBDR technical knowledge
   - Non-technical content: MUST come from project data source only
   - Do NOT fetch non-technical content from network
   - Verify all project-specific information matches provided data

## Examples

### Example 1: Basic Generation
```
User: 根据project-data/project-t-system生成最佳实践文档
Action: 
1. Verify project-data/project-t-system/project-info.md exists and is .md format
2. Read project data from project-data/project-t-system/
3. Extract key information (T-System, 3500+ VMs, VMware to HCS8.2)
4. Generate 2 documents (Chinese + English standard) with proper structure
5. Save to output/project-t-system/
6. Provide summary of generated files
```

### Example 2: With Specific Focus
```
User: Generate HyperBDR best practices for SAP HANA DR project, focus on orchestration
Action:
1. Verify project data file is .md format
2. Generate standard versions with emphasis on orchestration
3. Include detailed orchestration configuration
4. Highlight orchestration-driven takeover process
5. Provide examples of orchestration workflows
6. Ensure all calculations are accurate
```

## Notes

- This skill focuses on HyperBDR architecture and capabilities
- Only standard version is generated (concise and complete versions removed)
- Bilingual documentation supports global teams
- Always verify extracted information matches project data
- Technical reference: Use https://docs.oneprocloud.com/ for HyperBDR technical knowledge
- Non-technical content: ONLY use project data source, do NOT fetch from network
- Strictly follow template structure (H1-H3 headings cannot be modified)
- Ensure all numerical calculations are accurate and validated
- Calculation tools can be customized based on specific requirements