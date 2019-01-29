# 1. csv, nested-list version
student1 = [
    ['id', 'name', 'phone', 'address'],
    [1, '홍길동', '01012345678', '서울'],
    [2, '전우치', '01098765432', '부산']
    ]
    
# 2. json, dictionary version
student2 = [
    {'id' : 1, 'name': '홍길동', 'phone': '01012345678', 'address': '서울'},
    {'id' : 2, 'name': '전우치', 'phone': '01098765432', 'address': '부산'}
]

# 3. object version
class Student:
    def __init__(self, id, name, phone, address):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address
    
student3 = [
    Student(1, '홍길동', '01012345678', '서울'),
    Student(2, '전우치', '01098765432', '부산')
    ]
    
    
# # Create
# Student.new()

# # Read
# Student.get()

# # Update
# Student.update()

# # Delete
# Student.destroy()