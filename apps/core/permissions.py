from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication


class AuthenticatedJWT:
    authentication_classes = [SessionAuthentication, JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]