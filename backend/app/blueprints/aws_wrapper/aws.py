import boto3


class AWSFactory:
    def __init__(self, aws_type):
        self.aws_type = aws_type

    def generate_client(self):
        if self.aws_type == "s3":
            return S3()
        elif self.aws_type == "dynamodb":
            return Dynamo()
        else:
            raise ValueError("Invalid AWS type")


class AWSClient:
    def __init__(self):
        self.client = None

    def list(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def create(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def delete(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def confirm_connection(self):
        raise NotImplementedError("Subclass must implement abstract method")


class S3(AWSClient):
    def __init__(self):
        super().__init__()
        self.client = boto3.client("s3")

    def list(self):
        response = self.client.list_buckets()
        print("S3 buckets:")
        for bucket in response['Buckets']:
            print(f"- {bucket['Name']}")

    def confirm_connection(self):
        try:
            self.client.list_buckets()
            print("S3 connection successful")
            return True
        except Exception as e:
            print(f"S3 connection failed: {str(e)}")
            return False


class Dynamo(AWSClient):
    def __init__(self):
        super().__init__()
        self.client = boto3.client("dynamodb")

    def confirm_connection(self):
        try:
            response = self.client.list_tables()
            print(f"DynamoDB connection successful. Tables found: {response['TableNames']}")
            return True
        except Exception as e:
            print(f"DynamoDB connection failed: {str(e)}")
            return False

    def list(self):
        try:
            response = self.client.list_tables()
            print("DynamoDB tables:")
            for table in response["TableNames"]:
                print(f"- {table}")
        except Exception as e:
            print(f"Error listing DynamoDB tables: {str(e)}")


def main():
    # S3 example
    s3 = AWSFactory("s3").generate_client()
    if s3.confirm_connection():
        s3.list()

    print("\n" + "-"*50 + "\n")

    # DynamoDB example
    dynamodb = AWSFactory("dynamodb").generate_client()
    if dynamodb.confirm_connection():
        dynamodb.list()


if __name__ == "__main__":
    main()