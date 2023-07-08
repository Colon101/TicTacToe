# Install required Python packages
$packages = @(
    "tk",
    "pyinstaller"
)

foreach ($package in $packages) {
    Write-Host "Installing $package..."
    pip install $package
}