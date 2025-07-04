"""
Local Image Generator - No API Keys Required
==========================================

Creates artistic images from text prompts using local Python libraries.
Uses PIL (Pillow), random patterns, gradients, and text rendering.

Author: AI Assistant
Date: July 4, 2025
"""

import os
import random
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from datetime import datetime
import colorsys

class LocalImageGenerator:
    """Generate artistic images locally without requiring API keys"""
    
    def __init__(self, output_dir="generated_images"):
        """Initialize the local image generator"""
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Color themes for different prompt types
        self.color_themes = {
            'nature': ['#228B22', '#32CD32', '#90EE90', '#006400', '#8FBC8F'],
            'ocean': ['#006994', '#4682B4', '#87CEEB', '#1E90FF', '#00CED1'],
            'sunset': ['#FF6347', '#FF8C00', '#FFD700', '#FF69B4', '#DC143C'],
            'space': ['#191970', '#4B0082', '#8B008B', '#9400D3', '#000080'],
            'forest': ['#228B22', '#006400', '#8B4513', '#2E8B57', '#556B2F'],
            'city': ['#696969', '#2F4F4F', '#708090', '#778899', '#A9A9A9'],
            'fire': ['#FF4500', '#FF6347', '#FF8C00', '#FFD700', '#DC143C'],
            'ice': ['#B0E0E6', '#87CEEB', '#ADD8E6', '#E0FFFF', '#F0F8FF'],
            'magic': ['#9370DB', '#BA55D3', '#DA70D6', '#EE82EE', '#DDA0DD'],
            'retro': ['#FF1493', '#00FFFF', '#FFFF00', '#FF69B4', '#00FF00']
        }
        
        print("🎨 Local Image Generator initialized!")
        print("✅ No API keys required - fully offline")
    
    def detect_theme(self, prompt):
        """Detect the theme from the prompt to choose appropriate colors"""
        prompt_lower = prompt.lower()
        
        theme_keywords = {
            'nature': ['tree', 'grass', 'plant', 'garden', 'nature', 'leaf'],
            'ocean': ['ocean', 'sea', 'water', 'wave', 'beach', 'blue'],
            'sunset': ['sunset', 'dawn', 'orange', 'warm', 'golden'],
            'space': ['space', 'star', 'galaxy', 'cosmic', 'universe', 'nebula'],
            'forest': ['forest', 'wood', 'jungle', 'tree', 'green'],
            'city': ['city', 'urban', 'building', 'street', 'skyscraper'],
            'fire': ['fire', 'flame', 'hot', 'red', 'burning'],
            'ice': ['ice', 'cold', 'frozen', 'winter', 'snow'],
            'magic': ['magic', 'mystical', 'fantasy', 'enchanted', 'wizard'],
            'retro': ['retro', 'neon', 'cyberpunk', '80s', 'synthwave']
        }
        
        # Count keyword matches for each theme
        theme_scores = {}
        for theme, keywords in theme_keywords.items():
            score = sum(1 for keyword in keywords if keyword in prompt_lower)
            if score > 0:
                theme_scores[theme] = score
        
        # Return theme with highest score, or random theme if no matches
        if theme_scores:
            return max(theme_scores.items(), key=lambda x: x[1])[0]
        else:
            return random.choice(list(self.color_themes.keys()))
    
    def generate_gradient_background(self, width, height, colors):
        """Generate a gradient background"""
        image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(image)
        
        # Choose gradient direction
        gradient_type = random.choice(['horizontal', 'vertical', 'diagonal', 'radial'])
        
        if gradient_type == 'horizontal':
            for x in range(width):
                ratio = x / width
                color = self.blend_colors(colors[0], colors[1], ratio)
                draw.line([(x, 0), (x, height)], fill=color)
                
        elif gradient_type == 'vertical':
            for y in range(height):
                ratio = y / height
                color = self.blend_colors(colors[0], colors[1], ratio)
                draw.line([(0, y), (width, y)], fill=color)
                
        elif gradient_type == 'diagonal':
            for y in range(height):
                for x in range(width):
                    ratio = (x + y) / (width + height)
                    color = self.blend_colors(colors[0], colors[1], ratio)
                    draw.point((x, y), fill=color)
                    
        elif gradient_type == 'radial':
            center_x, center_y = width // 2, height // 2
            max_distance = math.sqrt(center_x**2 + center_y**2)
            
            for y in range(height):
                for x in range(width):
                    distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
                    ratio = min(distance / max_distance, 1.0)
                    color = self.blend_colors(colors[0], colors[1], ratio)
                    draw.point((x, y), fill=color)
        
        return image
    
    def blend_colors(self, color1, color2, ratio):
        """Blend two hex colors based on ratio (0.0 to 1.0)"""
        # Convert hex to RGB
        r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
        r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
        
        # Blend
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        
        return (r, g, b)
    
    def add_geometric_patterns(self, image, colors):
        """Add geometric patterns to the image"""
        draw = ImageDraw.Draw(image)
        width, height = image.size
        
        pattern_type = random.choice(['circles', 'rectangles', 'triangles', 'lines'])
        num_shapes = random.randint(5, 15)
        
        for _ in range(num_shapes):
            color = random.choice(colors)
            alpha = random.randint(50, 150)
            
            # Create a semi-transparent overlay
            overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
            overlay_draw = ImageDraw.Draw(overlay)
            
            if pattern_type == 'circles':
                x = random.randint(0, width)
                y = random.randint(0, height)
                radius = random.randint(20, 100)
                
                # Convert hex to RGB and add alpha
                r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
                circle_color = (r, g, b, alpha)
                
                overlay_draw.ellipse([x-radius, y-radius, x+radius, y+radius], 
                                   fill=circle_color)
                
            elif pattern_type == 'rectangles':
                x1 = random.randint(0, width//2)
                y1 = random.randint(0, height//2)
                x2 = random.randint(x1, width)
                y2 = random.randint(y1, height)
                
                r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
                rect_color = (r, g, b, alpha)
                
                overlay_draw.rectangle([x1, y1, x2, y2], fill=rect_color)
            
            # Composite the overlay onto the main image
            image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
        
        return image
    
    def add_text_overlay(self, image, prompt):
        """Add artistic text overlay to the image"""
        draw = ImageDraw.Draw(image)
        width, height = image.size
        
        # Try to load a font, fallback to default
        try:
            # Try different font sizes
            for font_size in [60, 48, 36, 24]:
                try:
                    font = ImageFont.truetype("arial.ttf", font_size)
                    break
                except:
                    continue
            else:
                font = ImageFont.load_default()
        except:
            font = ImageFont.load_default()
        
        # Prepare text (use first few words of prompt)
        words = prompt.split()[:3]  # Take first 3 words
        display_text = " ".join(words).upper()
        
        # Get text dimensions
        bbox = draw.textbbox((0, 0), display_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Position text
        text_positions = [
            (width//2 - text_width//2, 50),  # Top center
            (width//2 - text_width//2, height - text_height - 50),  # Bottom center
            (50, height//2 - text_height//2),  # Left center
            (width - text_width - 50, height//2 - text_height//2),  # Right center
        ]
        
        x, y = random.choice(text_positions)
        
        # Add text shadow
        shadow_offset = 3
        draw.text((x + shadow_offset, y + shadow_offset), display_text, 
                 fill='black', font=font)
        
        # Add main text
        draw.text((x, y), display_text, fill='white', font=font)
        
        return image
    
    def apply_artistic_effects(self, image):
        """Apply artistic effects to the image"""
        effects = ['blur', 'sharpen', 'emboss', 'edge_enhance', 'smooth']
        chosen_effect = random.choice(effects)
        
        if chosen_effect == 'blur':
            image = image.filter(ImageFilter.GaussianBlur(radius=1))
        elif chosen_effect == 'sharpen':
            image = image.filter(ImageFilter.SHARPEN)
        elif chosen_effect == 'emboss':
            image = image.filter(ImageFilter.EMBOSS)
        elif chosen_effect == 'edge_enhance':
            image = image.filter(ImageFilter.EDGE_ENHANCE)
        elif chosen_effect == 'smooth':
            image = image.filter(ImageFilter.SMOOTH)
        
        return image
    
    def create_abstract_art(self, width, height, colors):
        """Create abstract art patterns"""
        image = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(image)
        
        # Create random abstract shapes
        num_shapes = random.randint(10, 25)
        
        for _ in range(num_shapes):
            shape_type = random.choice(['ellipse', 'rectangle', 'polygon'])
            color = random.choice(colors)
            
            if shape_type == 'ellipse':
                x1 = random.randint(0, width//2)
                y1 = random.randint(0, height//2)
                x2 = random.randint(x1, width)
                y2 = random.randint(y1, height)
                draw.ellipse([x1, y1, x2, y2], fill=color)
                
            elif shape_type == 'rectangle':
                x1 = random.randint(0, width//2)
                y1 = random.randint(0, height//2)
                x2 = random.randint(x1, width)
                y2 = random.randint(y1, height)
                draw.rectangle([x1, y1, x2, y2], fill=color)
                
            elif shape_type == 'polygon':
                points = []
                num_points = random.randint(3, 6)
                for _ in range(num_points):
                    x = random.randint(0, width)
                    y = random.randint(0, height)
                    points.append((x, y))
                draw.polygon(points, fill=color)
        
        return image
    
    def generate_image(self, prompt, width=800, height=600, style='auto'):
        """
        Generate an artistic image based on the text prompt
        
        Args:
            prompt (str): Text description for the image
            width (int): Image width
            height (int): Image height
            style (str): Generation style - 'gradient', 'abstract', 'geometric', or 'auto'
        
        Returns:
            str: Path to the generated image
        """
        if not prompt or not prompt.strip():
            print("❌ Prompt cannot be empty")
            return None
        
        prompt = prompt.strip()
        print(f"🎨 Generating image for: '{prompt}'")
        
        # Detect theme and get colors
        theme = self.detect_theme(prompt)
        colors = self.color_themes[theme]
        print(f"🎭 Detected theme: {theme}")
        
        # Choose style
        if style == 'auto':
            style = random.choice(['gradient', 'abstract', 'geometric'])
        
        print(f"🖌️ Using style: {style}")
        
        try:
            # Generate base image based on style
            if style == 'gradient':
                image = self.generate_gradient_background(width, height, colors[:2])
                
            elif style == 'abstract':
                image = self.create_abstract_art(width, height, colors)
                
            elif style == 'geometric':
                # Start with solid color background
                bg_color = colors[0]
                r, g, b = int(bg_color[1:3], 16), int(bg_color[3:5], 16), int(bg_color[5:7], 16)
                image = Image.new('RGB', (width, height), (r, g, b))
                
                # Add geometric patterns
                image = self.add_geometric_patterns(image, colors[1:])
            
            # Add text overlay
            image = self.add_text_overlay(image, prompt)
            
            # Apply artistic effects
            image = self.apply_artistic_effects(image)
            
            # Save image
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"local_generated_{style}_{timestamp}.png"
            filepath = os.path.join(self.output_dir, filename)
            image.save(filepath)
            
            print(f"✅ Image generated successfully!")
            print(f"📁 Saved to: {filepath}")
            print(f"🎨 Theme: {theme} | Style: {style}")
            
            return filepath
            
        except Exception as e:
            print(f"❌ Error generating image: {e}")
            return None
    
    def batch_generate(self, prompts, **kwargs):
        """Generate multiple images from a list of prompts"""
        results = []
        total = len(prompts)
        
        print(f"🔄 Starting batch generation of {total} images...")
        
        for i, prompt in enumerate(prompts, 1):
            print(f"\n[{i}/{total}] Processing: '{prompt[:50]}...'")
            result = self.generate_image(prompt, **kwargs)
            results.append(result)
        
        successful = sum(1 for r in results if r is not None)
        print(f"\n📊 Batch generation complete!")
        print(f"✅ Successful: {successful}/{total}")
        
        return results

def main():
    """Interactive demo of the local image generator"""
    
    print("🎨 Local Image Generator")
    print("=" * 40)
    print("✅ No API keys required!")
    print("🖼️ Creates artistic images using local Python libraries")
    print()
    
    generator = LocalImageGenerator()
    
    # Example prompts
    example_prompts = [
        "Peaceful mountain landscape",
        "Abstract cosmic explosion",
        "Retro neon cityscape",
        "Magical forest glade",
        "Ocean waves at sunset",
        "Geometric rainbow patterns",
        "Mystical purple nebula",
        "Warm autumn colors",
        "Ice crystal formations",
        "Fire and flame patterns"
    ]
    
    try:
        print("Choose an option:")
        print("1. Generate from example prompts")
        print("2. Enter your own prompt")
        print("3. Batch generate examples")
        print("4. Style comparison (same prompt, different styles)")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            print("\nExample prompts:")
            for i, prompt in enumerate(example_prompts, 1):
                print(f"{i:2d}. {prompt}")
            
            try:
                idx = int(input(f"\nChoose prompt (1-{len(example_prompts)}): ")) - 1
                if 0 <= idx < len(example_prompts):
                    selected_prompt = example_prompts[idx]
                    generator.generate_image(selected_prompt)
                else:
                    print("❌ Invalid selection")
            except ValueError:
                print("❌ Please enter a valid number")
        
        elif choice == "2":
            custom_prompt = input("\nEnter your prompt: ").strip()
            if custom_prompt:
                # Ask for style preference
                print("\nChoose style:")
                print("1. Auto (random)")
                print("2. Gradient")
                print("3. Abstract")
                print("4. Geometric")
                
                style_choice = input("Style (1-4): ").strip()
                style_map = {'1': 'auto', '2': 'gradient', '3': 'abstract', '4': 'geometric'}
                style = style_map.get(style_choice, 'auto')
                
                generator.generate_image(custom_prompt, style=style)
            else:
                print("❌ Prompt cannot be empty")
        
        elif choice == "3":
            print(f"\n🔄 Batch generating {len(example_prompts)} images...")
            generator.batch_generate(example_prompts)
        
        elif choice == "4":
            prompt = input("\nEnter prompt for style comparison: ").strip()
            if prompt:
                print("\n🎨 Generating same prompt in different styles...")
                styles = ['gradient', 'abstract', 'geometric']
                for style in styles:
                    print(f"\nGenerating {style} style...")
                    generator.generate_image(prompt, style=style)
            else:
                print("❌ Prompt cannot be empty")
        
        else:
            print("❌ Invalid choice")
    
    except KeyboardInterrupt:
        print("\n\n👋 Generation cancelled by user")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
    
    print(f"\n📁 Check the '{generator.output_dir}' folder for your generated images!")
    print("🎉 Happy creating!")

if __name__ == "__main__":
    main()
