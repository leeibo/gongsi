# 表格OutputTableItem

1. 序号 number
2. 名称 name char*
3. 规格 specification char*
4. 级别 level char* 
5. 单位 unit char *  -->根|个|套
6. 数量 quantity int
7. 重量 weight float
8. 单价 price float
9. 合计 total float
10. 备注 remark

## 依赖关系

2,3-->4,5,7

F(1,2,3,6,8,9,10)

F(2,3,4,5,7)

## 数据模型OutputTableItem

1. 序号 number
2. 数量 quantity int
3. 单价 price float
4. 合计 total float
5. 备注 remark char*
6. 产品 project Project

# 产品Product

## 数据模型

1. 产品id id int auto
2. 名称 name char*
3. 规格 specification char*
4. 类型 class
5. 级别 level char* 
6. 单位 unit char *  -->根|个|套
7. 重量 weight float