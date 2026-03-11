# HyperBDR Best Practices Generator - 安装和使用指南

## 📦 技能包信息

**技能名称**: hyperbdr-best-practices-generator
**技能文件**: hyperbdr-best-practices-generator.skill
**文件大小**: 38 KB

**版本**: 1.0
**创建日期**: 2026-03-10

## 🚀 安装步骤

### 方法1: 通过Claude Code安装

1. 将 `hyperbdr-best-practices-generator.skill` 文件复制到您的技能目录
2. Claude Code会自动检测并加载该技能

### 方法2: 通过Claude.ai安装

1. 在Claude.ai中，找到技能管理界面
2. 点击"安装技能"或"导入技能"
3. 选择 `hyperbdr-best-practices-generator.skill` 文件
4. 等待安装完成

### 方法3: 手动安装

1. 将 `hyperbdr-best-practices-generator.skill` 解压
2. 将解压后的文件夹复制到您的技能目录
3. 重启Claude Code或Claude.ai

## 📖 技能目录结构

安装后，技能目录结构如下：

```
hyperbdr-best-practices-generator/
├── SKILL.md                          # 主技能文档
├── README.md                          # 用户指南
├── CREATION_SUMMARY.md                 # 创建总结
├── evals/
│   └── evals.json                    # 测试用例
├── references/
│   ├── hyperbdr-knowledge.md          # HyperBDR知识库
│   └── translation-guide.md           # 中英文翻译指南
├── assets/
│   └── templates/
│       ├── zh-concise-template.md     # 中文简明版
│       ├── en-concise-template.md     # 英文简明版
│       ├── zh-standard-template.md     # 中文标准版
│       ├── en-standard-template.md     # 英文标准版
│       ├── zh-complete-template.md     # 中文完整版
│       └── en-complete-template.md     # 英文完整版
└── scripts/
    └── generate_docs.py              # 文档生成脚本
```

## 💡 使用方法

### 基本使用

当您需要生成HyperBDR最佳实践文档时，可以使用以下任一方式触发技能：

#### 触发词

- "auto最佳实践"
- "最佳实践文档"
- "best practices"
- "HyperBDR best practices"
- "生成最佳实践文档"

#### 示例提示

**中文示例**:
```
根据project-data/project-t-system生成最佳实践文档
```

```
auto最佳实践 for T-System项目
```

```
使用project-data/project-t-system目录下的项目数据生成HyperBDR容灾最佳实践文档，需要生成三种版本（简明、标准、完整），中英文双语输出
```

**英文示例**:
```
Generate HyperBDR best practices documentation from project-data/project-t-system
```

```
Create bilingual best practices documentation for the Mexico migration project
```

### 输入要求

#### 项目数据结构

```
project-data/
└── [项目名称]/
    ├── 项目信息.md          # 项目数据文件（Markdown格式）
    └── images/                  # 架构图和图片
```

#### 项目数据格式

项目数据文件应包含以下章节：

1. **项目背景** (项目背景)
   - 客户名称及背景
   - 迁移需求
   - 业务系统类型
   - 主机规格
   - 备份策略等

2. **架构图** (架构图)
   - 架构图的视觉表示
   - 图片引用在 `images/` 目录中

3. **客户挑战** (客户挑战)
   - 具体的痛点和困难
   - 技术约束
   - 业务需求

4. **解决方案** (解决方案)
   - 使用的HyperBDR能力
   - 实施方法
   - 技术优势

5. **客户收益** (客户收益)
   - 交付的业务价值
   - 运营改进
   - 成本节约

6. **项目亮点展示** (项目亮点展示)
   - 关键成就
   - 创新点
   - 成功指标

### 输出格式

技能将生成以下结构的文档：

```
output/
└── [项目名称]/
    ├── [项目名称]最佳实践-简明-中文.md
    ├── [项目名称]Best Practices-Concise-English.md
    ├── [项目名称]最佳实践-标准-中文.md
    ├── [项目名称]Best Practices-Standard-English.md
    ├── [项目名称]最佳实践-完整-中文.md
    ├── [项目名称]Best Practices-Complete-English.md
    └── images/              # 从项目数据复制
```

## 📄 文档版本说明

### 简明版 (Concise Version)

**文件名**:
- `[项目名称]最佳实践-简明-中文.md`
- `[项目名称]Best Practices-Concise-English.md`

**特点**:
- 快速参考指南
- 包含关键要点和表格
- 简短描述（1-2句）
- 仅包含关键指标
- 适合快速了解项目

**使用场景**:
- 快速项目概览
- 高层汇报
- 快速参考

### 标准版 (Standard Version)

**文件名**:
- `[项目名称]最佳实践-标准-中文.md`
- `[项目名称]Best Practices-Standard-English.md`

**`特点**:
- 详细实施指南
- 包含详细说明（2-3句）
- 逐步指导
- 完整的表格
- 实用示例
- 适合实施参考

**使用场景**:
- 项目实施指导
- 技术团队参考
- 详细学习材料

### 完整版 (Complete Version)

**文件名**:
- `[项目名称]最佳实践-完整-中文.md`
- `[项目名称]Best Practices-Complete-English.md`

**特点**:
- 所有标准版内容
- 故障排除章节
- 安全与合规章节
- 参考资源章节
- 附录（术语表、配置清单、联系人、版本历史）
- 适合深度学习和参考

**使用场景**:
- 深度技术学习
- 问题排查
- 完整参考文档
- 知识库建设

## 🎯 文档结构

每个生成的文档都包含以下6个主要章节：

### 1. 项目概述 (项目概述)
- 客户和场景详情（表格格式）
- 业务特点
- 系统规模（主机数量、存储）
- 源/目标环境
- 容灾目标
- HyperBDR核心价值（标准版/完整版）

### 2. 业务挑战与HyperBDR解决方案 (业务挑战与HyperBDR解决方案)
- 系统复杂度
- RPO/RTO要求
- 目标环境成本
- 带宽和同步
- 部署和运维复杂度

### 3. HyperBDR方案与架构 (HyperBDR方案与架构)
- 总体思路
- 架构要点:
  - 生产环境详情
  - 容灾环境详情
  - 存储层配置
  - 复制策略
- 架构图（从项目数据引用）
- 表格显示HyperBDR核心能力及其应用和价值

### 4. 实施要点与演练最佳实践 (实施要点与演练最佳实践)
- 数据复制阶段
- 容灾演练和接管阶段
- 最佳实践和建议

### 5. 关键成果与指标 (关键成果与指标)
- 性能指标
- RTO/RPO成就
- 成本优化结果

### 6. 项目总结 (项目总结)
- 关键成就
- 项目价值
- 典型场景

## 🔧 HyperBDR核心能力

技能整合了来自 https://docs.oneprocloud.com/ 的知识：

### 网络规划
- 迁移与容灾网络规划
- SaaS网络通信
- AWS跨区域容灾

### 策略管理
- 策略最佳实践
- 前置/后置脚本
- 基于策略的同步

### 编排
- HyperBDR编排最佳实践
- Boot in Cloud一键恢复
- 并行恢复和依赖管理

### VMware无代理迁移
- VMware无代理迁移
- 自动化驱动适配
- 批量主机迁移

### 对象存储技术
- 使用对象存储的Boot in Cloud
- 成本优化
- 弹性云能力

### 故障回切
- 云到VMware的故障回切
- 容灾故障回切最佳实践

## ⚙️ 常见问题

### Q1: 技能没有触发？

**A**: 确保您使用了触发词，如"auto最佳实践"、"最佳实践文档"、"best practices"等。技能描述已优化以提高触发准确率。

### Q2: 项目数据格式不正确？

**A**: 确保项目数据文件包含所有必需的章节（项目背景、架构图、客户挑战、解决方案、客户收益、项目亮点展示）。使用标准的Markdown格式。

### Q3: 生成的文档内容不完整？

**A**: 检查项目数据是否包含足够的信息。技能会提取可用信息并填充模板，如果某些信息缺失，可能需要手动补充。

### Q4: 英文翻译不准确？

**A**: 技能使用了翻译指南来确保术语一致性。如果发现翻译问题，可以手动编辑英文文档。

### Q5: 如何自定义模板？

**A**: 您可以编辑 `assets/templates/` 目录下的模板文件，自定义文档结构和内容。

## 📞 支持和帮助

### 文档资源
- **HyperBDR文档**: https://docs.oneprocloud.com/
- **技术实践**: https://docs.oneprocloud.com/userguide/technical-practices/
- **项目实践**: https://docs.oneprocloud.com/userguide/project-practices/
- **HyperBDR手册**: https://docs.oneprocloud.com/userguide/dr/

### 支持资源
- **AI支持**: https://ai.oneprocloud.com/chat/qWGp3yX8ain2550b
- **获取支持**: https://support.oneprocloud.com/
- **FAQ**: https://qa.oneprocloud.com/

### 工具
- **计算器**: https://calculator.oneprocloud.com/

## 🔄 更新和维护

### 检查更新

定期检查技能更新以获取新功能和改进。

### 自定义和扩展

您可以根据需要自定义技能：
- 修改模板文件
- 添加新的测试用例
- 扩展HyperBDR知识库
- 自定义翻译指南

### 反馈

如果您有任何问题或建议，请通过以下方式反馈：
- GitHub Issues（如果技能在GitHub上）
- HyperBDR支持团队
- AI支持聊天

## 📝 使用示例

### 示例1: 基本使用

```
用户: 根据project-data/project-t-system生成最佳实践文档

Claude: ✓ 开始生成HyperBDR最佳实践文档...
      
      读取项目数据: project-data/project-t-system/T-System墨西哥迁移项目案例信息收集.md
      提取关键信息: T-System, 3500+ VMs, VMware到HCS8.2
      应用HyperBDR知识: 批量迁移、无代理、自动化驱动适配
      生成文档: 6个文档（3版本×2语言）
      
      ✓ 文档生成成功！
      
      生成的文件:
        - T-System墨西哥迁移项目最佳实践-简明-中文.md
        - T-System Mexico Migration Project Best Practices-Concise-English.md
        - T-System墨西哥迁移项目最佳实践-标准-中文.md
        - T-System Mexico Migration Project Best Practices-Standard-English.md
        - T-System墨西哥迁移项目最佳实践-完整-中文.md
        - T-System Mexico Migration Project Best Practices-Complete-English.md
      
      输出目录: output/project-t-system/
```

### 示例2: 指定版本

```
用户: 生成T-System项目的标准版最佳实践文档

Claude: ✓ 生成标准版文档...
      
      中文: T-System墨西哥迁移项目最佳实践-标准-中文.md
      英文: T-System Mexico Migration Project Best Practices-Standard-English.md
      
      ✓ 完成！
```

### 示例3: 批量处理

```
用户: 为所有项目生成最佳实践文档

Claude: ✓ 批量生成文档...
      
      项目1: project-t-system
        ✓ 生成6个文档
      
      项目2: project-sap-hana
        ✓ 生成6个文档
      
      项目3: project-multi-cloud
        ✓ 生成6个文档
      
      ✓ 总计生成18个文档
```

## ✅ 验证清单

安装后，请验证以下项目：

- [ ] 技能文件已正确安装
- [ ] Claude Code/Claude.ai已识别技能
- [ ] 使用触发词可以触发技能
- [ ] 可以成功生成文档
- [ ] 生成的文档格式正确
-` [ ] 中英文内容对应
- [ ] 所有6个文档都已生成

## 🎓 技能统计

- **总文件数**: 15+
- **总代码行数**: 3000+
- **模板文件**: 6个
- **测试用例**: 3个
- **断言数量**: 20+
- **文档页数**: 8+
- **技能包大小**: 38 KB

## 🌟 技能亮点

1. **全面的知识库**: 整合了HyperBDR官方文档知识
2. **双语文档支持**: 原生中英文生成
3. **多版本输出**: 三个版本满足不同使用场景
4. **模板化生成**: 基于模板生成，确保格式一致
5. **经过测试**: 包含全面的测试用例和断言
6. **文档完善**: 详细的README和指南

## 📄 许可证

本技能是HyperBDR生态系统的一部分，遵循相同的许可条款。

---

**技能版本**: 1.0
**最后更新**: 2026-03-10
**维护者**: HyperBDR团队

**感谢使用HyperBDR最佳实践文档生成技能！**