import requests

token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjlhNTE5MDc0NmU5M2JhZTI0OWIyYWE3YzJhYTRlMzA2M2UzNDFlYzciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZmFzdGFwaWF1dGgtNmIwNWEiLCJhdWQiOiJmYXN0YXBpYXV0aC02YjA1YSIsImF1dGhfdGltZSI6MTY5NjY3NTQwOSwidXNlcl9pZCI6IlBvZnJJT1FuakRWdTdPNkdLcURtVVM2em42UDIiLCJzdWIiOiJQb2ZySU9RbmpEVnU3TzZHS3FEbVVTNnpuNlAyIiwiaWF0IjoxNjk2Njc1NDA5LCJleHAiOjE2OTY2NzkwMDksImVtYWlsIjoic2FtcGxlQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJzYW1wbGVAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.iYEaeRyqQ2Oaul7EsiADMYt1IhtBww74cErEnPuWpd7-UT4LkLg9G2Pn5exWN2Ahh8PFdecUAeD8nE8CI7HIioaQMh43QK9m_IVHMwhdp71-L7SQ6r1QjOCgkU3R5Td-RwhElH_YK0ap9823489VAybSfadFLCXJ6ezuNd6i5-C-nxyVient4-wx9pGxfyexcPLej3mi11PfVsmMw5wmWFEM2AelekziXuRBPuCaY6WaOtgG6_asGOAdCLOHBlr6CJ7nuoLXaWRug7UANOS_3LhcJQS3DsL-kaIyc8xvZ-Xv2KIlWRicpl-Pv7S21-OdrN8csjJjMKlQvMftZYdpgQ"

def test_ping():
    headers = {
        "authorization": token
    }

    response = requests.post("http://127.0.0.1:8000/ping", headers = headers)

    return response.text

print(test_ping())