from django.http import HttpResponse

from django.template import RequestContext, loader
from django.shortcuts import render_to_response

import PIL
import PIL.Image
import StringIO
from django.shortcuts import render


def index(request):
    
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context, Motherfucker"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('lucy/index.html', context_dict, context) 
    

    









def graph(request):


    from matplotlib import pylab
    import numpy as np
    import matplotlib.pyplot as plt


    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)
    x3 = np.linspace(2.0, 4.0)
    x4 = np.linspace(0.0, 7.0)


    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)
    y3 = np.cos(2 * np.pi * x2)
    y4 = np.cos(2 * np.pi * x2)


    plt.subplot(2, 2, 1)
    plt.plot(x1, y1, 'yo-',)
    plt.title('Temperature')
    plt.ylabel('Celcius')

    plt.subplot(2, 2, 2)
    plt.plot(x3, y3, 'yo-')
    plt.title('Druck')
    plt.ylabel('Bar')
    
    plt.subplot(2, 2, 4)
    plt.plot(x2, y2, 'r.-')
    plt.title('4te Variable')
    plt.ylabel('unknown')
    
    plt.subplot(2, 2, 3)
    plt.plot(x3, y3, 'yo-')
    plt.title('Feuchtigkeit')
    plt.ylabel('Digits')

    
    
  
    
    
    buffer = StringIO.StringIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    graphIMG = PIL.Image.fromstring("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save(buffer,"PNG")
    pylab.close()
    
    return HttpResponse(buffer.getvalue(), mimetype = "image/png")