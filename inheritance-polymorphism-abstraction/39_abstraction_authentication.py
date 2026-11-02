from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def authenticate(self, credentials):
        pass

class PasswordAuth(Authentication):
    def __init__(self, valid_password):
        self.valid_password = valid_password

    def authenticate(self, credentials):
        return credentials == self.valid_password

class OTPAuth(Authentication):
    def __init__(self, valid_otp):
        self.valid_otp = valid_otp

    def authenticate(self, credentials):
        return credentials == self.valid_otp

class BiometricAuth(Authentication):
    def __init__(self, registered_hash):
        self.registered_hash = registered_hash

    def authenticate(self, credentials):
        return credentials == self.registered_hash

def login_user(auth_service, input_cred):
    if auth_service.authenticate(input_cred):
        print(f'{auth_service.__class__.__name__}: Authentication Successful!')
    else:
        print(f'{auth_service.__class__.__name__}: Authentication Failed!')

login_user(PasswordAuth('Secret@123'), 'Secret@123')
login_user(OTPAuth('987654'), '987654')
login_user(BiometricAuth('FINGERPRINT_HASH_AA99'), 'WRONG_HASH')
