import os
from Projects.ImageGenerator import LocalImageGenerator

# Initialize the generator
generator = LocalImageGenerator()

# Generate the image
result = generator.generate_image("Mystical forest with glowing mushrooms")

if result:
    print(f"✅ Image saved: {result}")
    print(f"📁 Full path: {os.path.abspath(result)}")
    print(f"📂 Output directory: {generator.output_dir}")
    
    # Show current working directory for reference
    print(f"💻 Current directory: {os.getcwd()}")
    
    # Check if file exists and show size
    if os.path.exists(result):
        file_size = os.path.getsize(result) / 1024  # Size in KB
        print(f"📏 File size: {file_size:.1f} KB")
        
        # Try to open the image (Windows)
        try:
            if os.name == 'nt':  # Windows
                os.startfile(result)
                print("🖼️ Opening image...")
            elif os.name == 'posix':  # macOS/Linux
                import subprocess
                if os.uname().sysname == 'Darwin':  # macOS
                    subprocess.run(['open', result])
                else:  # Linux
                    subprocess.run(['xdg-open', result])
                print("🖼️ Opening image...")
        except Exception as e:
            print(f"⚠️ Could not auto-open image: {e}")
            print("💡 You can manually open the image from the path shown above")
else:
    print("❌ Failed to generate image")