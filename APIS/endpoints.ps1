$listerner = New-Object System.Net.HttpListener
$listerner.Prefixes.Add("http://localhost:8080/")
$listerner.Start()

# Import-Module for each service
./Init-Module.ps1
"Listening ..."

while ($true) {
    $context = $listerner.GetContext()

    # Capture the details about the request
    $request = $context.Request

    # Setup a place to deliver a response
    $response = $context.Response

    Write-Host "Request received Context : 
    $($context | ConvertTo-Json -Depth 100)"

    switch ($request.UrlReferrer) {
        "/end" {  }
        "/v1/virtualmachine" {  }
        Default {  }
    }

    if ($request.Url -match "/end$") {
        break
    } else {
        # Send a response
        $response.StatusCode = 200
        $response.StatusDescription = "OK"
        $response.ContentType = "text/plain"
        $response.ContentLength64 = 0
        $response.OutputStream.Close()
    }
}

$listerner.Stop()