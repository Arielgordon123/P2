import boto3
import P1

def get_s3_resources():
    buckets = []
    s3 = boto3.resource('s3')

    for bucket in s3.buckets.all():
        buckets.append(bucket.name)
    
    return buckets 
def get_weather(lat, lon):
    return P1.get_weather(lat, lon)

def main():
    print("P2 main:")
    print("P2 call to => get_weather:", P1.get_weather(32.0853,34.7818))
    print("P2 call to => get s3 resources",get_s3_resources())

if __name__ == "__main__":
    main()