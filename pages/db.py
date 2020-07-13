import os, firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "webp-bf95a",
    "private_key_id": "8efbfa76d5906a896385264d8eb3b5e7b744c5c2",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDMF082tnKFwRf9\nMrCoBHQxUAXVYEp8OvJuKdCKe9B2likhARspp0Kct/13N1KdyYmyyzIO1PDlHTVA\nboToZMz0FADSRlQX6fOnNs+lK4+DZMvZ/9QxMm+nKtBql01ywduVPZTjU41MQND2\no3g3x0Xx0IxiTZzJtUDLXpOrhDGIiKyC3u1AU7NreMhJvOWeExlrOSkgHzmdJkmr\nuPJS4wSYNlljVy5cMCdru2cTi8731xxiGTAilXVGnS+PTSBt8xysI1R23a/0w55A\nYPgPvhYJj/c79BqRahz102gofXAjiaLh8kM6GcHzR2UosjjGzJK6OKvPRXwMFYs7\nBPmmVDgHAgMBAAECggEARTL+E9IGwJ05Egu25DEmaHX2lGOivb6K5plc8SeMBjlh\n1qP2XsgsiNDFqz9hzsg/3RSSc3718ulVXfRbMiTDbVq+8I0SBE255I9sFlfPwEBT\n8iWQ/+FXBDo7EnkctHVQi6imq/FvblRnxcilgVwatiP9BXPFXosLXilCLpyS4vTA\nlL8Tul4s5fUphczY5ho5u5ezT4hGkFwFyngsa31P3lJfn9Ip+5PkVFawMfdJF6Uj\nMdSDTMptnr6Ly+5DeJfj9NsTpxEmXixCPsJRQSvdQzJP601t4bL/4QhI0fMAyqSB\nt+rS7VBKJ8AUW3uiH0VuaQXZAqRsYbhJtXzVbdFP4QKBgQD96Awi5Hk3wxFqfE5O\n/5pdkZum56sWPeRS7Op63fNWwjSWc8VuuxjiLHtdl+PpfcEvsKmPzs9h/pSkrA4s\ntIcUmhRV+hI2y0NNT1Ff3p/vogljBmdJIyfaMOqyQxrC4amc72LfUsArKxv3aPuJ\nCd+sLCnV+Av4zZwPAnA/Z9ohEQKBgQDNxhxAiEczP8XOmfcNwSW02+/8as24tO4L\nuvKP4miMpjR51czUIKAxvW95DYZKP6lvxnbtydoSBg2DYdti16vHxtzuW2AwKeWx\nZGYmG+JFtIvI8Y0ghLPQI3T8ypQ3724Ue03FQGEAvJmoKd1mfau1gZ/Mj5t+0YcZ\nAgZGnY9HlwKBgAYw6ErZg1MmwH/2M/qdJOhvKnpxX6yVKcIT4MvKKarN5XZdsEy4\n5yxspT1s/LOuy00cY6YMBuZ+zKUPRPE2Ha0U7LYD+Pm5DxUNgBB0XzX6n3v4pgAU\niV46nx5loHtsATTAaYrEe8cRsAbiWm/G+9s44HRFLhWM/ecnyhDhuWHhAoGAYGeg\ndNtkAC6wjcq0ZE1JTSJ9nNSs7QxXOkervJ1mPf7gNvRjsj5WzvbhcuVTNRX+W8+v\niFg5QphzXEpMblJ8uGwCtek5d1cptaJD+Ta3G9EqbEo+xC1n0OvLs2N1bX9PI2lh\nVjiDOcUieBalE49tEuxX4Y6mWxPvJ1g7eHn41qECgYAEN/vITl1Ox3/j9fYmdo/j\nI29MMrm0SJQ+lixd1gwHVn7C0bTd1k8mZnkPrMHAjmhD70mejfL5HUAjvKDcBg42\nqlD8n1gZCE+eEGghtxY61yyuENdIbyt8GJRHCF6dWdH9QeRTRzTapqN2764Ry/99\n2hvcTzBIetlhhxFYKwikxA==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-6x61s@webp-bf95a.iam.gserviceaccount.com",
    "client_id": "109516319999443633043",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-6x61s%40webp-bf95a.iam.gserviceaccount.com"
})
    default_app = firebase_admin.initialize_app(cred)

db = firestore.client()