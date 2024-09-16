from bson import ObjectId
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
mydatabase = client["userdatabase"]
mycollection = mydatabase["users"]

##### CRUD ALL FUNCTIONS.....

###Insert 25 users
user = [
  { "id": 1, "name": "Avi Negi", "age": 19, "projects": [{"name": "Project X", "budget": 12000}, {"name": "Project Y", "budget": 8000}], "skills":["C","C++","Python","MongoDB","JavaScript"], "email": "avi.negi@email.com", "state": "Uttarakhand", "department": "Devlopment", "salary": 95000 },
  { "id": 2, "name": "Emily Johnson", "age": 28, "projects": [{"name": "Project Z", "budget": 5000}], "skills":["Python","SQL"], "email": "emily.johnson@email.com", "state": "Texas", "department": "Marketing", "salary": 62000 },
  { "id": 3, "name": "Michael Williams", "age": 45, "projects": [{"name": "Project A", "budget": 10000}, {"name": "Project B", "budget": 15000}], "skills":["Python","MongoDB","JavaScript"], "email": "michael.williams@email.com", "state": "New York", "department": "Devlopment", "salary": 95000 },
  { "id": 4, "name": "Sarah Brown", "age": 31, "email": "sarah.brown@email.com", "state": "Florida", "department": "HR", "salary": 70000 },
  { "id": 5, "name": "David Jones", "age": 38, "email": "david.jones@email.com", "state": "Illinois", "department": "Sales", "salary": 78000 },
  { "id": 6, "name": "Amanda Miller", "age": 29, "email": "amanda.miller@email.com", "state": "Georgia", "department": "Marketing", "salary": 63500 },
  { "id": 7, "name": "Matthew Davis", "age": 40, "email": "matthew.davis@email.com", "state": "Ohio", "department": "Devlopment", "salary": 90000 },
  { "id": 8, "name": "Jessica Wilson", "age": 27, "email": "jessica.wilson@email.com", "state": "Michigan", "department": "HR", "salary": 68000 },
  { "id": 9, "name": "Daniel Martinez", "age": 50, "email": "daniel.martinez@email.com", "state": "Colorado", "department": "Sales", "salary": 85500 },
  { "id": 10, "name": "Megan Anderson", "age": 33, "email": "megan.anderson@email.com", "state": "Washington", "department": "Marketing", "salary": 65000 },
  { "id": 11, "name": "Ryan Thomas", "age": 36, "email": "ryan.thomas@email.com", "state": "Arizona", "department": "Sales", "salary": 80000 },
  { "id": 12, "name": "Rebecca Taylor", "age": 24, "email": "rebecca.taylor@email.com", "state": "Nevada", "department": "Devlopment", "salary": 82000 },
  { "id": 13, "name": "Andrew Moore", "age": 43, "email": "andrew.moore@email.com", "state": "Oregon", "department": "HR", "salary": 72500 },
  { "id": 14, "name": "Lauren Jackson", "age": 32, "email": "lauren.jackson@email.com", "state": "Utah", "department": "Marketing", "salary": 66500 },
  { "id": 15, "name": "Jason White", "age": 39, "email": "jason.white@email.com", "state": "Virginia", "department": "Sales", "salary": 79000 },
  { "id": 16, "name": "Kimberly Harris", "age": 26, "email": "kimberly.harris@email.com", "state": "Kansas", "department": "Devlopment", "salary": 84000 },
  { "id": 17, "name": "Joshua Clark", "age": 48, "email": "joshua.clark@email.com", "state": "Indiana", "department": "Marketing", "salary": 69000 },
  { "id": 18, "name": "Stephanie Lewis", "age": 35, "email": "stephanie.lewis@email.com", "state": "Missouri", "department": "HR", "salary": 73500 },
  { "id": 19, "name": "Christopher Lee", "age": 42, "email": "christopher.lee@email.com", "state": "Pennsylvania", "department": "Engineering", "salary": 92000 },
  { "id": 20, "name": "Melissa Walker", "age": 29, "email": "melissa.walker@email.com", "state": "North Carolina", "department": "Sales", "salary": 77000 },
  { "id": 21, "name": "Benjamin Hall", "age": 31, "email": "benjamin.hall@email.com", "state": "Kentucky", "department": "Marketing", "salary": 67000 },
  { "id": 22, "name": "Samantha Allen", "age": 37, "email": "samantha.allen@email.com", "state": "Wisconsin", "department": "HR", "salary": 71000 },
  { "id": 23, "name": "Nathan Young", "age": 44, "email": "nathan.young@email.com", "state": "Tennessee", "department": "Sales", "salary": 81000 },
  { "id": 24, "name": "Ashley King", "age": 30, "email": "ashley.king@email.com", "state": "Alabama", "department": "Engineering", "salary": 86000 },
  { "id": 25, "name": "Brandon Scott", "age": 41, "email": "brandon.scott@email.com", "state": "Oklahoma", "department": "Marketing", "salary": 64500 }
]
mycollection.insert_many(user)



### FIND ALL QUARIES
## Find all documents in the collection
results = mycollection.find()
## Print each document
for i in results:
    print(i)


##To Find Specific Users by Name
result = mycollection.find_one({"name": "Avi Negi"})
print(result)


##To find the Users a Specific Department
result = mycollection.find({"department": "Devlopment"})
for i in result:
    print(i)


##sort and limit----The sort() method is used to specify the order in which documents should be returned. 
##                      You can sort documents in ascending (1) or descending (-1) order.
##                  The limit() method restricts the number of documents returned from a query.
result = mycollection.find().sort("age", -1).limit(5)
for i in result:
    print(i)


##$gt----To find Users with Salary Greater than 80,000
result = mycollection.find({"salary": {"$gt": 80000}})
for i in result:
    print(i)


##$lt----To find Users with salary less than 80,000
result = mycollection.find({"salary": {"$lt": 80000}})
for i in result:
    print(i)


##$lte----Users with salary less than or equal to 80,000
result = mycollection.find({"salary": {"$lte": 80000}})
for i in result:
    print(i)


##$gte----Users with Salary Greater Than or Equal to 80,000
result = mycollection.find({"salary": {"$gte": 80000}})
for i in result:
    print(i)


##$elemMatch-----dealing with arrays in MongoDB. If you have other conditions or nested structures, 
##          the $eleMatch approach can be used to query for specific elements in an array.
result = mycollection.find({
    "projects": {
        "$elemMatch": {
            "budget": {"$gt": 10000}
        }
    }
})
for i in result:
    print(i)


##$all-----The $all operator in MongoDB is used to match an array field that contains all the specified elements. 
##       It ensures that all elements in the provided array exist in the target array field.
result = mycollection.find({
    "skills":{
        "$all": ["Python", "MongoDB"]
        }
})
for i in result:
    print(i)


##$in-----The $in operator in MongoDB is used to match documents where a specified field's value exists in a given array of possible values. 
##         Unlike $all, which requires all values to be present in an array, 
##          $in matches if any of the values are present.
result = mycollection.find({
    "state":{
        "$in": ["Uttarakhand", "New York", "Texas"]
    }
})
for i in result:
    print(i)


##$and----The $and operator in MongoDB is used to combine multiple conditions, 
##         and it matches documents that satisfy all of the specified conditions.
result = mycollection.find({
    "$and": [
        {"department": "Devlopment"},
        {"salary": {"$gt": 80000}}
    ]
})
for i in result:
    print(i)


##$or-----The $or operator in MongoDB is used to match documents that satisfy any of the specified conditions.
##         and if at least one of them is true, the document will be included in the result set.
result = mycollection.find({
    "$or":[
        {"state": "Uttarakhand"},
        {"salary": {"$lt": 70000}}
    ]
})
for i in result:
    print(i)


##$and with multiple $or-----allows you to build complex queries where some conditions must be met together,
##                             while others are flexible and can be met in any combination.
result = mycollection.find({
    "$or": [
        {"$and":[
            {"state": "Uttarakhand"},
            {"$or":[
                {"salary": {"gt": 80000}},
                {"age": {"lt": 30}}
            ]}
        ]},
        {"$and":[
            {"state": "Texas"},
            {"salary": {"$gte": 60000, "$lte": 80000}}
        ]}
    ]
})
for i in result:
    print(i)


##$not-----The $not operator in MongoDB is used to exclude documents that match the specified
##         condition. It is used to negate the condition specified in the query.
result = mycollection.find({
    "department": { "$not": { "$eq": "HR" } }
})
for i in result:
    print(i)


##$type------The $type operator in MongoDB is used to query documents based on the type of a field's value. 
##             It allows you to match documents where the field is of a specified data type.
result = mycollection.find({
    "age": { "$type": "int" }
})
for i in result:
    print(i)



###REPLACE QUARIES
##Define the filter and replacement document
filter = { "id": 5}
replacement = {
    "id": 5,
    "name": "David Jones",
    "age": 40,
    "email": "jones@email.com",
    "state": "illinois",
    "department": "Sales",
    "salary": 80000
}
##Replace the document
result = mycollection.replace_one(filter, replacement, upsert = False)
print(f"Matched {result.matched_count} document(s)")
print(f"Modified {result.modified_count} document(s)")



###UPDATE ALL QUARIES
##Using $set-----Sets the value of a field. If the field does not exist, it will be created. 
document_id = ObjectId("66e2cc5aead6ab93462af0cb")
filter = { "_id": document_id }
update = {
    "$set": {
        "id": 4,
        "salary": 60000,
        "department": "HR"
    }
}
result = mycollection.update_one(filter, update)
print(f"Matched {result.matched_count} document(s)")
print(f"Modified {result.modified_count} document(s)")


##$upset----Removes a field from a document
filter = {"id": 26}
update= {
    "$unset": {"age": "49"}
}
result = mycollection.update_one(filter, update)
print(f"Matched {result.matched_count} document(s)")
print(f"Modified {result.modified_count} document(s)")


##Using $inc-----Increments the value of a field by a specified amount.
filter = {"id": 6}
update = {
    "$inc": {"salary": 1000}
}
result = mycollection.update_one(filter, update)
print(f"Matched {result.matched_count} document(s)")
print(f"Modified {result.modified_count} document(s)")


##$push-----Adds an item to an array field.
filter = {"id": 7}
update = {
    "$push": {"skills": ["Project Management", "ML"]}
}
result = mycollection.update_one(filter, update)
print(f"Matched {result.matched_count} document(s)")
print(f"Modified {result.modified_count} document(s)")


##$pull-----Removes an item from an array field.
filter = {"id": 7}
update = {
    "$pull": {"skills": "Project Management"}
}
result = mycollection.update_one(filter, update)
print(f"Matched {result.matched_count} document(s)")
print(f"Modified {result.modified_count} document(s)")


##$upsert-----when you want to ensure that a document is created if it does not already exist
filter = { "id": 26 }
update = {
    "$set": {
        "name": "Samantha Carter",
        "age": "49",
        "email": "samantha.carter@email.com",
        "state": "California",
        "department": "Marketing",
        "salary": 65000
    }
}
result = mycollection.update_one(filter, update, upsert=True)
print(f"Matched {result.matched_count} document(s)")
print(f"Modified {result.modified_count} document(s)")
print(f"Upserted ID: {result.upserted_id}")


##Add a field in 26 database(using $set)
filter = {"id": 26}
update = {
    "$set": {"phone": 1234567890}
}
result = mycollection.update_one(filter, update)
print(f"Matched {result.matched_count} document(s)")
print(f"Modified {result.modified_count} document(s)")


##UPDATE MANY
filter = {"department": "Engineering"}
update = {
    "$set": {"bonus": 500}
}
result = mycollection.update_many(filter,update)
print(f"Matched {result.matched_count} document(s)")
print(f"Modified {result.modified_count} document(s)")



###DELETE QUARIES
## delete_one-----deletes the first document that matches the filter criteria.
filter = {"id": 32}
result = mycollection.delete_one(filter)
print(f"Deleted {result.deleted_count} document(s)")


## delete_many-----deletes all documents that match the filter criteria.
filter = {"department": "Site"}
result = mycollection.delete_many(filter)
print(f"Deleted {result.deleted_count} document(s)")

## drop whole collection
mycollection.drop()


###AGGREGATION PIPELINES
##$match----the $match stage in an aggregation pipeline is used to filter 
##          documents based on specified criteria.
pipeline = [
    { "$match": { "department": "Sales", "salary": { "$gt": 80000 } } }
]
result = mycollection.aggregate(pipeline)
for i in result:
  print(i)


##$group----the $group stage in an aggregation pipeline is used to group documents by 
##                 a specified field and perform aggregation operations 
##             like sum, count, average, min, max, etc., on the grouped data.
pipeline = [
  {
    "$group": {
      "_id": "$department",
      "totalSalary": { "$sum": "$salary" }
    }
  }
]
result = mycollection.aggregate(pipeline)
for i in result:
  print(i)


##$sort----the $sort stage in an aggregation pipeline is used to sort the documents.
pipeline = [
  { "$sort": { "salary": -1 } }  # Sort by salary in descending order
]
result = mycollection.aggregate(pipeline)
for i in result:
  print(i)


##$limit----the $limit stage in an aggregation pipeline is used to restrict 
##       the number of documents returned by the pipeline to a specified number.
pipeline = [
  { "$limit": 5 }  # Limit the result to 5 documents
]
result = mycollection.aggregate(pipeline)
for i in result:
  print(i)


##$project---- the $project stage in an aggregation pipeline is used to include, exclude, 
##                   or reshape fields in the output documents.
pipeline = [
  { 
    "$project": { 
      "_id": 0,  # Exclude the _id field
      "name": 1,  # Include the name field
      "department": 1,  # Include the department field
      "salary": 1  # Include the salary field
    } 
  }
]
result = mycollection.aggregate(pipeline)
for i in result:
    print(i)


##$set----the $set stage in an aggregation pipeline is used to add new fields or update existing fields in documents.
pipeline = [
  {
    "$set": {
      "bonus": { "$multiply": ["$salary", 0.10] }  # Add bonus as 10% of salary
    }
  }
]
result = mycollection.aggregate(pipeline)
for i in result:
  print(i)


##$count----$count is used in aggregation pipelines to count the number of documents.
pipeline = [
  { "$match": { "department": "Engineering" } },
  { "$count": "engineeringUsers" }
]
result = mycollection.aggregate(pipeline)
for i in result:
  print(i)


##$out----the $out stage in an aggregation pipeline is used to write the results of the aggregation to a new collection.
pipeline = [
  { 
    "$group": { 
      "_id": "$department",
      "averageSalary": { "$avg": "$salary" }
    }
  },
  { "$out": "department_averages" }
]
mycollection.aggregate(pipeline)
print("Aggregation result has been written to the 'department_averages' collection.")
# Retrieve and print the results from the 'department_averages' collection
result = mydatabase["department_averages"].find()
for doc in result:
  print(doc)
## [END]