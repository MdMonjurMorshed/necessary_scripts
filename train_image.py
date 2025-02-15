
## django code 
class TestImage(APIView):
    def post(self,request,*args,**kwargs):
        company_uuid = kwargs.get('company_uuid')
        employees = Employee.objects.filter(company_uuid=company_uuid)
        for employee in employees:
            trainee_image = TraineeImage.objects.filter(employee_id=employee).order_by('-created_at').first()
            if not trainee_image:
                continue
            # print(trainee_image.aws_image_id) 
            # print(employee.uuid) 
            print(trainee_image.updated_at)
            

            # base64_image=image_url_to_base64(trainee_image.digitalocean_link)
                            
            # url = AWS_SERVICE_URL + "/api/v2/face-recog/faces/add/"
            # payload = {
            #     "company_uuid": str(employee.company_uuid),
            #     "image_name": str(employee.uuid),
            #     "image": base64_image
            # }
            # headers = {"Content-Type": "application/json"}
            
            # aws_response = requests.request(
            #     "POST", url, json=payload, headers=headers)
            
            # print("aws response: ",aws_response)

            # if aws_response.status_code == 200:
            #     aws_response_data = aws_response.json()
            #     aws_image_id = aws_response_data.get('data').get('face_id')
            #     url = "https://transmitter.evidentbd.com/api/v1/upload/global/image"
            #     payload = {
            #         "service": "attendancekeeper",
            #         "encoded_image": base64_image
            #     }
            #     headers = {
            #         "Content-Type": "application/json",
            #         "SECRET-KEY": "GYGWYERY58454FDS4FD8V487FF8WQ8EF11D88W1D"
            #     }
            #     digitalocan_response = requests.request(
            #         "POST", url, json=payload, headers=headers)
                
            #     print('digitalocan response: ',digitalocan_response)
            #     print('transmiter service json response',digitalocan_response.json())
            #     if digitalocan_response.status_code == 200:
            #         response_data = digitalocan_response.json()
            #         digitalocan_degitalocan_link = response_data.get(
            #         'data').get('edge_url')

            #         trainee_image.aws_image_id=aws_image_id
            #         trainee_image.digitalocean_link=digitalocan_degitalocan_link
            #         trainee_image.save()
            #     else:
            #         print(f'digital ocan link:{digitalocan_degitalocan_link} face id: {aws_image_id}')
            #         print(f'face not added for {employee.uuid}')    
            #         # new_trainee_image = TraineeImage.objects.create(
            #         #     employee=new_employee, aws_image_id=aws_image_id, digitalocean_link=digitalocan_degitalocan_link)
            # else:
            #     print(f'face not added for {employee.uuid}')
        return Response()