error = Exception("Some error occurred.")
print(type(error))
answer = {
    "message": "Message about error",
    "detail": "Error occurred" + str(error),
    "deep_info": f"{error}",
}
print(answer.get("message"))
print(answer.get("detail"))
print(answer.get("deep_info"))
