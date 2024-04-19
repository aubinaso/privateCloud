$listOfModule = Get-ChildItem -Path .\APIS -Recurse | Where-Object { $_.GetType().Name -eq "DirectoryInfo" }

$psm1Files = @()

foreach ($module in $listOfModule) {
    $modulePath = $module.FullName
    $moduleFiles = Get-ChildItem -Path $modulePath -Recurse -Filter "*.psm1" | Where-Object { $_.GetType().Name -eq "FileInfo" }
    $moduleFiles | ForEach-Object {
        Import-Module $_.FullName
    }
}