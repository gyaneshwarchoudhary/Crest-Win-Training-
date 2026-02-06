"""
Docstring for Day-06.__Doc__
 - Exception & Context Manager
 - File handling
 - Http Fundamentals
 - curl & jq
"""
"""
exception handling:
    - gracefully handle error earlier 
    - error and exception 
    - excetion: alter the flow of program
            - Baseexception, exception, stopiteration, arithmeticerror, valueerror, typeerror, zerodivisionerror, key error, etc
    - try, except, else, finally
    - catching specific exceptions: ValueError, TypeError, ZeroDivisionError, FileNotFoundError, KeyError, etc
    - Catching multiple excetions: except (ValueError, TypeError) as e:
    - Catching all handlers
    - 
"""




"""
File Handling:
 - process of operation on file 
 - need of file handling:
    - to store data permanently
    - access files like .txt, .csv, .json, .xml, .html, .pdf, .docx, etc
    - to automate tasks 
    - to process large files
  - Encoding: 
    - process of converting data into a specific format for storage or transmission
    - require decoding to get the og data
    - char enc- utf-8, ascii etc, audio enc- mp3, wav,aac , video enc- mp4, h.264, hevc. Image enc-jpeg ,gif , others - base64, hex, etc
  - python open() function:
    - open internally stored files
    - syntax : open(filename, mode), r(dafault), w(if not then create and overtite it)
              a add(append, if not then create and add data), x(create a specific file,if FileExistsError then error ), b(binary mode, files like images), t(text mode, default), + (read and write mode eg: r+, w+)
    - file.close()
    - file reading, using read(), readline(), readlines()
    - file writing: using write() and writelines() 
    - with statement (context manager) to handle file automatically
    - context manager: relies on context manager __enter__(): Acquires the resource and returns it.
        __exit__(): Releases the resource when the block exits

"""


"""
Http fundamentals:
    - HTTP: HyperText Transfer Protocol, load webpage using hypertext links. 
    - application layer protocol, built on top of TCP/IP, stateless protocol, client-server model, request-response cycle
    protocol: set of rules, to communicate with each other, for example internet protocol 
         - IPSec, icmp, igmp 
    - components of HTTP:
        - url, http version type, method, request headers, body
        - header: stores inf in key value pairs 
"""

"""
Curl & jq:
    - cli tool and liberay, industry standard 
    why it is used: 
        - test Apis 
        - Automation 
        - Dubugging
        - platform independent
    - Commands:
        - curl url get the website content 
        - saving a file curl -o filename url
        - sending data curl -x POST URL -H header -d data
        - checking headers curl -I url 
    jq 
        - lightwieght and flexible cl json processor
        - getting unreadle massive wall of text
        - prettyfying 
        - filtering 
        - Transforming: map, ruduce and can change the shape of the data 
        - Automation 
"""