`openssl req -new -x509 -days 365 -nodes -out tsacert.pem -keyout client_cert.pem`
`openssl x509 -x509toreq -in tsacert.pem -out cert.pem -signkey client_cert.pem`

# Private Key
Simple private key

```
% openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout cert.pem¬
Generating a 1024 bit RSA private key¬
.......++++++¬
.............................++++++¬
writing new private key to 'cert.pem'¬
-----¬
You are about to be asked to enter information that will be incorporated¬
into your certificate request.¬
What you are about to enter is what is called a Distinguished Name or a DN.¬
There are quite a few fields but you can leave some blank¬
For some fields there will be a default value,¬
If you enter '.', the field will be left blank.¬
-----¬
Country Name (2 letter code) [AU]:US¬
State or Province Name (full name) [Some-State]:MyState¬
Locality Name (eg, city) []:Some City¬
Organization Name (eg, company) [Internet Widgits Pty Ltd]:My Organization, Inc.¬
Organizational Unit Name (eg, section) []:My Group¬
Common Name (eg, YOUR name) []:myserver.mygroup.myorganization.com¬
Email Address []:ops@myserver.mygroup.myorganization.com¬
%¬

```
```
openssl genpkey -algorithm EC -out eckey.pem -pkeyopt ec_paramgen_curve:P-384 -pkeyopt
ec_param_enc:named_curve

openssl ec -in eckey.pem -des3 -out des3ecky.pem
openssl enc -iter 5 -in eckey.pem -out iter5_eckey.pem
openssl ec -in des-ede3-cbc-eccrsa.pem -pubout -out des-ede3-cbc-eccrsa.pub
openssl req -new -x509 -days 365 -out cert-des.pem -keyout cert-des.pem
```
```
openssl genpkey -algorithm EC -out eckey.pem -pkeyopt ec_paramgen_curve:P-384 -pkeyopt
ec_param_enc:named_curve
openssl ec -in eckey.pem -aes-256-cbc -out cbc-eccrsa.pem
openssl enc -in eckey.pem -iter 5 -out cbc-eccrsa-5.pem
openssl ec -in cbc-eccrsa-5.pem -pubout -out cbc-eccrsa-5.pub
openssl req -new -x509 -days 365 -nodes -out cert-cbc-eccrsa-5.pem -keyout cert-cbc-eccrsa-5.pem
```

### DSA

```
openssl genpkey -genparam -algorithm DSA -out dsap.pem -pkeyopt dsa_paramgen_bits:4096
```
```
openssl genpkey -paramfile dsap.pem -out dsakey.pem
```


### EC
```
openssl genpkey -algorithm EC -out eckey.pem -pkeyopt ec_paramgen_curve:P-384 -pkeyopt
ec_param_enc:named_curve
```

### DH
REALLY SLOW!!!
```
openssl genpkey -genparam -algorithm DH -out dhp.pem -pkeyopt dh_paramgen_prime_len:2048
openssl genpkey -paramfile dhp.pem -out dhkey.pem
```


##### DH X9.42
not working on v1.0.1u (2016)

```
openssl genpkey -genparam -algorithm DH -out dhpx.pem -pkeyopt dh_paramgen_prime_len:2048 -pkeyopt
dh_paramgen_type:1
openssl genpkey -paramfile dhpx.pem -out dhxkey.pem
```


##### RFC5114 2048 bit 224 bit subgroup
```
openssl genpkey -genparam -algorithm DH -out dhp2.pem -pkeyopt dh_rfc5114:2
openssl genpkey -paramfile dhp.pem -out dhkey2.pem
```


### RSA
```
openssl genpkey -algorithm RSA -out key.pem -pkeyopt rsa_keygen_bits:4096 -pkeyopt
rsa_keygen_pubexp:3
```

###### with aes 128 encrypted passphrase:
```
openssl genpkey -algorithm RSA -out key.pem aes-128-cbc -pass pass:hello
```



now we have our custom private key we can use to create cert and/or req??
ithink...

```
openssl req -key <key.pem> -out rsareq.pem -days 365 -nodes
```

```
openssl req -newkey dsa:dsap.pem -keyout dsakey.pem -out dsareq.pem \
-days 365 -nodes
```


######  encrypt private key using triple DES:
```
openssl ec -in key.pem -des3 -out keyout.pem
```


###### print key
```
openssl ec -in key.pem -text -nooout
```

###### print pubkey
```
openssl ec -in key.pem -pubout -out pubkey.pem
```

###### change encoding
```
openssl ec -in key.pem -param_enc explicit -out keyout.pem
```

###### change point conversion ??
```

```
openssl ec -in key.pem -conv_form compressed -out keyout.pem
```
Convert a certificate to a certificate request:

        openssl x509 -x509toreq -in cert.pem -out req.pem -signkey key.pem

       Convert a certificate request into a self signed certificate using
       extensions for a CA:

        openssl x509 -req -in careq.pem -extfile openssl.cnf -extensions v3_ca \
               -signkey key.pem -out cacert.pem

```
###### -newcert
certificate in `newcert.pem`
private key in `newkey.pem`


`openssl -new -x509 -keyout newkey.pem -out newcert.pem -days 365`  


###### -newreq
Request in `newreq.pem`
private key in `newkey.pem`

`openssl req -new -keyout newkey.pem -out newreq.pem -days 365`  


###### -newreq NoDES
Request (and private key) is in `newreq.pem`

`openssl req -new -nodes -keyout newreq.pem -out newreq.pem -days 365`

###### -newca

`/etc/ssl/demoCA`

`/etc/ssl/demoCA/private`
CA keys

`/etc/ssl/demoCA/certs`

`/etc/ssl/demoCA/newcerts

`/etc/ssl/demoCA/crl

*if ca cert*
    demoCA/cacert.pem
`openssl x509 -in demoCA/cacert.pem -noout -next_serial -out demoCA/serial`

*else make ca cert*


######  cacert req
```
    openssl req -new -keyout demoCA/private/cakey.pem \
    -out demoCA/careq.pem
```

```
    openssl ca <openssl.cnf> -create_serial -out demoCA/cacert.pem -days 1065 -batch \
    -keyfile demoCA/private/cakey.pem -selfsign \
    -extensions v3_ca \
    -infiles demoCA/careq.pem
```


###### sign cert req

*-xsign*
```
openssl ca <openssl.cnf> -policy policy_anything -infiles newreq.pem
```

*-pkcs12*
```
openssl pks12 -config <openssl.cnf>  -in newcert.pem -inkey newreq.lpem \
-certfile demoCA/cacert.pem -out newcert.p12 -export -name "My Certificate"
```
*-sign*
```
openssl ca <openssl.cnf> </openssl> -policy policy_anything -out newcert.pem -infiles newreq.pem
```

*-signca*
```
openssl ca <openssl.cnf> -policy policy_anything -out newcert.pem \
-extensions v3_ca -infiles newreq.pem
```

*-signcert*

```
openssl x509 -x509toreq -in newreq.pem -signkey newreq.pem -out tmp.pem
openssl ca <openssl.cnf> -policy policy_anything -out newcert.pem -infiles tmp.pem \
&& cat newcert.pem
```

*-verify example*
```
openssl verify -CAfile demoCA/cacert.pem
```
*or*
```
openssl verify -CAfile <cert.pem>
```




