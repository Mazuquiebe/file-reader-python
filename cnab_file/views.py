from rest_framework.views import APIView, Request, Response, status
from utils.cnab_reader import CNABReader
from .models import  CNABFile 
from .serializer import CNABDataSerializer


class CNABDataView(APIView):

    def post(self, request:Request) -> Response:

        file = request.FILES.get('file')

        cnab = CNABFile.objects.create(file=file)
        cnab.save()

        reader = CNABReader(f'uploads/{cnab.file}')
        cnab_data = reader.get_cnab_data()

        serializer = CNABDataSerializer(data=cnab_data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
        

