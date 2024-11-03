from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["local"]
employees_collection = db["employees"]

sample_employees = [
    {"name": "Hunk", "position": "軟體工程師", "age": 28, "department": "資訊科技部"},
    {"name": "Jile", "position": "人力資源專員", "age": 34, "department": "人力資源部"},
    {"name": "May", "position": "行銷經理", "age": 42, "department": "行銷部"},
    {"name": "Coco", "position": "財務分析師", "age": 30, "department": "財務部"},
    {"name": "Tedy", "position": "產品經理", "age": 37, "department": "產品部"},
    {"name": "John Smith", "position": "Software Engineer", "age": 28, "department": "IT Department"},
    {"name": "Emily Johnson", "position": "HR Specialist", "age": 34, "department": "Human Resources"},
    {"name": "Michael Brown", "position": "Marketing Manager", "age": 42, "department": "Marketing"},
    {"name": "Jessica Davis", "position": "Financial Analyst", "age": 30, "department": "Finance"},
    {"name": "William Wilson", "position": "Product Manager", "age": 37, "department": "Product"},
    {"name": "Olivia Taylor", "position": "Sales Executive", "age": 29, "department": "Sales"},
    {"name": "James Anderson", "position": "Data Scientist", "age": 31, "department": "Data Analytics"},
    {"name": "Sophia Thomas", "position": "Operations Manager", "age": 40, "department": "Operations"},
    {"name": "Liam Jackson", "position": "Web Developer", "age": 27, "department": "IT Department"},
    {"name": "Isabella White", "position": "Customer Support Agent", "age": 25, "department": "Customer Service"}
    
]

# 插入資料到集合中
employees_collection.insert_many(sample_employees)
print("員工資料已成功插入")
