from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import qrcode
from io import BytesIO

def home(request):
    if request.method == 'POST':
        # Retrieve job order data from the form
        job_order = request.POST.get('job_order', '')

        if job_order:
            # Create QR code instance
            qr = qrcode.QRCode(version=1, box_size=100, border=2)

            # Add data to the QR code
            qr.add_data(job_order)

            # Generate the QR code
            qr.make(fit=True)

            # Create an image from the QR code
            img = qr.make_image(back_color="black", fill_color="white")
            # Save the QR code as a PNG file with the job order name
            image_name = f"{job_order}.png"
            buffer = BytesIO()
            img.save(buffer)
            buffer.seek(0)

            # Serve the QR code as a response
            response = HttpResponse(buffer, content_type='image/png')
            response['Content-Disposition'] = f'attachment; filename="{image_name}"'
            return response

    return render(request, 'home.html')