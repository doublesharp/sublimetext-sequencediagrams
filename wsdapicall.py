from threading import Thread
import urllib  
import urllib2

class WebSequenceDiagramAPICall(Thread):
    '''
    Wraps an API request to WSD in a thread to prevent
    sublime text from blocking.
    '''

    ENDPOINT = 'http://www.websequencediagrams.com/'

    def __init__(self, wsd_request, timeout = 5):
        '''Initializes the API call before sending the message.''' 

        self.wsd_request = wsd_request
        self.timeout = timeout  
        self.result = None

        super(WebSequenceDiagramAPICall, self).__init__()

    def run(self):
        '''Executes the thread. Makes the API request.'''
        
        #TODO: Handle Errors from API Call (Syntax Errors)
        try:  
            data = urllib.urlencode(self.wsd_request.__dict__)  
            request = urllib2.Request(self.ENDPOINT, data)  
            response = urllib2.urlopen(request, timeout = self.timeout)  
            self.result = response.read()
        except (urllib2.HTTPError) as (e):
            error = 'HTTP ERROR: {0}'.format(str(e.code))  
            sublime.error_message(error)  
            self.result = False
        except (urllib2.URLError) as (e):  
            error = 'URL ERROR: {0}'.format(str(e.reason))
            sublime.error_message(error)  
            self.result = False