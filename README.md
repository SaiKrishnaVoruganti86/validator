changed name from   pattern: '^[A-Za-z0-9_.-]*$' to   pattern: '^[A-Za-z0-9.,-_/]*$'  
changed id from   pattern: '^((urn:sdx:topology:)[A-Za-z0-9_.:-]*$)' to   pattern: '^urn:sdx:topology:[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  
model_version previously only type: string, now added as pattern: ^2\.0\.0$  
timestamp changed from format: date-time to pattern: '^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])T([01]\d|2[0-3]):([0-5]\d):([0-5]\d)Z$'  

changes on nodes:  
changed name from pattern: '^[A-Za-z0-9_.-]*$' to pattern: '^[a-zA-Z0-9.,\-_\/]{1,30}$'  
changed id from pattern: '^((urn:sdx:node:)[A-Za-z0-9_.\:/-]*$)'to '^urn:sdx:node:[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}:[a-zA-Z0-9.,\-_\/]{1,30}$'  
added:   
    status:  
        type: string  
        enum: [up, down, error]    
added:   
    state:  
        type: string  
        enum: [enabled, disabled, maintenance]  

changes on port:  
changed name from pattern: '^[A-Za-z0-9_.\:/-]*$' to pattern: '^[a-zA-Z0-9.,\-_\/]{1,30}$'   
changed port id from     
pattern: '^((urn:sdx:port:)[A-Za-z0-9_.\:/-]*$)'  
to    
^urn:sdx:port:[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}:[a-zA-Z0-9.,\-_\/]{1,30}:[a-zA-Z0-9.,\-_\/]{1,30}$    
changed node from pattern: '^((urn:sdx:node:)[A-Za-z0-9_.\:/-]*$)' to '^urn:sdx:node:[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}:[a-zA-Z0-9.,\-_\/]{1,30}$'  
removed short_name    
removed label_range  
changed mtu from   
        mtu:  
          type: integer  
          format: int32  

to  
        mtu:  
          type: integer  
          #format: int32  
          minimum: 1500  
          maximum: 10000  
          default: 1500  

changed nni from    
        nni:  
          type: string  
to  
        nni:  
          type: string  
          pattern: '^(urn:sdx:link:[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}:[a-zA-Z0-9.,\-_\/]{1,30})?$|^$'  

added 'maintenance' in state enum  

changes on Link:     
changed name from     
        name:      
          type: string      
          minLength: 3     
          maxLength: 30     
          pattern: '^[A-Za-z0-9_./\:-]*$'  
to    
        name:    
          type: string    
          pattern: '^[a-zA-Z0-9.,\-_\/]{1,30}$'     

changed id from pattern: '^((urn:sdx:link:)[A-Za-z0-9_.\:/-]*$)'    
to    
'^urn:sdx:link:[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}:[a-zA-Z0-9.,\-_\/]{1,30}+$'    

changed type from enum: ['intra','inter'] to enum: ['intra']    

changes on Location:  
added iso3166_2_lvl4 in required.   
address changed from   
        address:  
          type: string  
to  
        address:  
          type: string  
          pattern: '^[\x00-\x7F]{1,255}$'  
latitude and longitude changed from   
          type: number  
          minimum: -90.0  
          maximum: 90.0  
to  
          type: string  
          pattern: '^(-?(90(\.0+)?|[1-8]?\d(\.\d+)?))$'  






