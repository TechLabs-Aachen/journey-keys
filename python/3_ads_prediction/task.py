# Challenge 3: Implement Ads Click prediction!

# Replace the email string with the email you used to register for Techlabs!
# This is required to generated your submission key.
EMAIL = "max_mustermann@gmail.com"

def transform(data):
    # TODO: Implement me!
    # This function receives the a dataset as a pandas dataframe and should return a transformed dataframe
    # You can use this function to perform normalizations or any data preprocessing you want!
    return data

def train(traindata):
    # TODO: Implement me!
    # Implement any model you want but don't go to crazy with the complexity!
    # This function should return a model that can be used for prediction.
    # It will receive the data after transformation by the `transform` function
    return None


def predict(model, data):
    # TODO: Implement me!
    # This funciton should return the predictions for a dataframe `data`
    # `model` will be the Model return by your `train` function
    # Note that data will already be transformed by the `transform` function
    return None

def validate_helper(val_data):
    # TODO: Implement me!
    # Depending on your transform, you may have to change this implementation
    # This function should extract the labels from the a dataframe (or whatever your
    # `transform` function returns for labels)
    # Expected return: Flat 1d array of labels
    return val_data["Purchased"]

if __name__ == "__main__":
    import base64
    eval(compile(base64.b64decode("ZGVmIFRMX05TX19nZW5LZXkocGFzc3BocmFzZSwgc2VjcmV0KToKICAgIGltcG9ydCBiYXNlNjQKICAgIHN1cGVyX3NlY3JldCA9ICJDQVRDSF9tZV9pZl95b3VfY2FuIUJ1dF9ZT1VfV09OVCFCZWNhdXNlX3RoaXNfaXMhU1VQRVJfU0VDUkVUISIKICAgIGtleSA9IGJ5dGVzKGEgXiBiICBmb3IgYSwgYiBpbiB6aXAocGFzc3BocmFzZS5lbmNvZGUoKSwgc3VwZXJfc2VjcmV0LmVuY29kZSgpKSkKICAgIGtleSA9IGJ5dGVzKGEgXiBiIGZvciBhLCBiIGluIHppcChrZXksIHNlY3JldC5lbmNvZGUoKSkpCiAgICBrZXkgPSBiYXNlNjQudXJsc2FmZV9iNjRlbmNvZGUoa2V5KQogICAgcmV0dXJuIGtleS5kZWNvZGUoKQoKZGVmIFRMX05TX19nZXRfZGF0YShkYXRhX3BhdGg9X19maWxlX18pOgogICAgaW1wb3J0IHBhbmRhcyBhcyBwZAogICAgdHJhaW5fY3N2ID0gcGQucmVhZF9jc3YoZiJ7ZGF0YV9wYXRofS9hZHNfdHJhaW5kYXRhLmNzdiIpCiAgICB0ZXN0X2NzdiA9IHBkLnJlYWRfY3N2KGYie2RhdGFfcGF0aH0vYWRzX3Rlc3RkYXRhLmNzdiIpCiAgICByZXR1cm4gdHJhaW5fY3N2LCB0ZXN0X2NzdgoKZGVmIFRMX05TX19ldmFsKGNsZiwgdGVzdCk6CiAgICBmcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgY29uZnVzaW9uX21hdHJpeAogICAgbWF0cml4ID0gY29uZnVzaW9uX21hdHJpeCh2YWxpZGF0ZV9oZWxwZXIodGVzdCksIHByZWRpY3QoY2xmLCB0ZXN0KSkKICAgIGVycm9ycyA9IG1hdHJpeFswXVsxXSArIG1hdHJpeFsxXVswXQogICAgcmV0dXJuIGVycm9ycwoKCmRlZiBUTF9OU19fY2hlY2soZGF0YV9wYXRoPV9fZmlsZV9fKToKICAgIGltcG9ydCBvcwogICAgaW1wb3J0IHBhbmRhcyBhcyBwZAogICAgZGF0YV9wYXRoID0gb3MucGF0aC5kaXJuYW1lKGRhdGFfcGF0aCkKICAgIHRyYWluZHMsIHRlc3RkcyA9IFRMX05TX19nZXRfZGF0YShkYXRhX3BhdGgpCiAgICB0cmFpbmRzID0gdHJhbnNmb3JtKHRyYWluZHMpCiAgICB0ZXN0ZHMgPSB0cmFuc2Zvcm0odGVzdGRzKQogICAgbW9kZWwgPSB0cmFpbih0cmFpbmRzKQoKICAgIGVycm9ycyA9IFRMX05TX19ldmFsKG1vZGVsLCB0ZXN0ZHMpCgogICAgcHJpbnQoZiJGYWxzZS1wb3NpdGl2ZXMvZmFsc2UtbmVnYXRpdmVzOiB7ZXJyb3JzfSIpCiAgICBpZiBlcnJvcnMgPiA1IGFuZCBlcnJvcnMgPD0gMTE6CiAgICAgICAgc2VjcmV0ID0gVExfTlNfX2dlbktleShFTUFJTCwgIm5pY2VfeW91X2dvdF90aGVfcmlnaHRfa2V5IikKICAgICAgICBwcmludChmIkNvbmdyYXR1bGF0aW9ucyEgWW91IGFjaGlldmVkIGFuIGFjY2VwdGFibGUgbW9kZWwgcGVyZm9ybWFuY2UuIFlvdXIgc2VjcmV0IGtleSBpcyB7c2VjcmV0fSIpCiAgICAgICAgcmV0dXJuCiAgICBlbGlmIGVycm9ycyA+IDExOgogICAgICAgIHByaW50KCJZb3VyIG1vZGVsIHBlcmZvcm1hbmNlIGlzIG5vdCBnb29kIGVub3VnaCEgKEV4cGVjdGVkIHRvIGJlIGJldHRlciB0aGFuIDExKS4gWW91IGNhbiBkbyBiZXR0ZXIgOikiKSAKICAgICAgICByZXR1cm4KICAgIGVsc2U6CiAgICAgICAgcHJpbnQoIllvdXIgbW9kZWwgcGVyZm9ybWFuY2UgaXMgZ29vZCwgdG9vIGdvb2QgPyEgKElmIHlvdSBkaWQgbm90IGNoZWF0LCBwbGVhc2UgY29udGFjdCB1cyBvbiBzbGFjaykiKQogICAgICAgIHJldHVybgpUTF9OU19fY2hlY2soKQo="), "<string>", "exec"))
