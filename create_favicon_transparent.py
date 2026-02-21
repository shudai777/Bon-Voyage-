#!/usr/bin/env python3
"""
透過背景ファビコン生成スクリプト
Bon Voyage用のドローンアイコン（透過背景版）
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_transparent_favicon(size, filename):
    """透過背景のファビコンを生成"""
    
    # 透過背景の画像を作成（RGBA）
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 中央の円（白）
    center = size // 2
    circle_radius = size // 3
    draw.ellipse(
        [center - circle_radius, center - circle_radius,
         center + circle_radius, center + circle_radius],
        fill=(255, 255, 255, 255)
    )
    
    # プロペラ（4つの小さい円）- 白
    propeller_radius = size // 8
    propeller_distance = size // 2.5
    
    positions = [
        (center - propeller_distance, center - propeller_distance),  # 左上
        (center + propeller_distance, center - propeller_distance),  # 右上
        (center - propeller_distance, center + propeller_distance),  # 左下
        (center + propeller_distance, center + propeller_distance),  # 右下
    ]
    
    for x, y in positions:
        draw.ellipse(
            [x - propeller_radius, y - propeller_radius,
             x + propeller_radius, y + propeller_radius],
            fill=(255, 255, 255, 255)
        )
        
        # プロペラと中央を繋ぐ線（白）
        draw.line([center, center, x, y], fill=(255, 255, 255, 255), width=max(2, size//50))
    
    # 「BV」テキストを描画（青）
    try:
        # フォントサイズを調整
        font_size = size // 3
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "BV"
    # テキストのバウンディングボックスを取得
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # テキストを中央に配置（青色）
    text_x = center - text_width // 2
    text_y = center - text_height // 2 - size // 20
    draw.text((text_x, text_y), text, fill=(30, 115, 232, 255), font=font)
    
    # 保存
    img.save(filename, 'PNG')
    print(f"✓ {filename} を生成しました（{size}x{size}px, 透過背景）")

def create_transparent_favicon_with_blue_circle(size, filename):
    """透過背景 + 青い円のファビコンを生成"""
    
    # 透過背景の画像を作成（RGBA）
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 外側の青い円
    center = size // 2
    outer_radius = size // 2 - 2  # 少し余白を残す
    
    # グラデーション風の青い円（単色版）
    draw.ellipse(
        [center - outer_radius, center - outer_radius,
         center + outer_radius, center + outer_radius],
        fill=(30, 115, 232, 255)  # 青色
    )
    
    # 中央の白い円
    circle_radius = size // 3
    draw.ellipse(
        [center - circle_radius, center - circle_radius,
         center + circle_radius, center + circle_radius],
        fill=(255, 255, 255, 255)
    )
    
    # プロペラ（4つの小さい円）- 白
    propeller_radius = size // 8
    propeller_distance = size // 2.5
    
    positions = [
        (center - propeller_distance, center - propeller_distance),  # 左上
        (center + propeller_distance, center - propeller_distance),  # 右上
        (center - propeller_distance, center + propeller_distance),  # 左下
        (center + propeller_distance, center + propeller_distance),  # 右下
    ]
    
    for x, y in positions:
        draw.ellipse(
            [x - propeller_radius, y - propeller_radius,
             x + propeller_radius, y + propeller_radius],
            fill=(255, 255, 255, 255)
        )
        
        # プロペラと中央を繋ぐ線（白）
        draw.line([center, center, x, y], fill=(255, 255, 255, 255), width=max(2, size//50))
    
    # 「BV」テキストを描画（青）
    try:
        # フォントサイズを調整
        font_size = size // 3
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "BV"
    # テキストのバウンディングボックスを取得
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # テキストを中央に配置（青色）
    text_x = center - text_width // 2
    text_y = center - text_height // 2 - size // 20
    draw.text((text_x, text_y), text, fill=(30, 115, 232, 255), font=font)
    
    # 保存
    img.save(filename, 'PNG')
    print(f"✓ {filename} を生成しました（{size}x{size}px, 青い円背景）")

# メイン処理
if __name__ == "__main__":
    print("🎨 透過背景ファビコンを生成中...\n")
    
    # 完全透過背景版
    print("【完全透過背景版】")
    create_transparent_favicon(512, 'favicon-transparent.png')
    create_transparent_favicon(192, 'favicon-transparent-192.png')
    create_transparent_favicon(180, 'favicon-transparent-180.png')
    create_transparent_favicon(48, 'favicon-transparent-48.png')
    create_transparent_favicon(32, 'favicon-transparent-32.png')
    create_transparent_favicon(16, 'favicon-transparent-16.png')
    
    print("\n【青い円背景版（透過外側）】")
    # 青い円背景版（外側は透過）
    create_transparent_favicon_with_blue_circle(512, 'favicon-blue-circle.png')
    create_transparent_favicon_with_blue_circle(192, 'favicon-blue-circle-192.png')
    create_transparent_favicon_with_blue_circle(180, 'favicon-blue-circle-180.png')
    create_transparent_favicon_with_blue_circle(48, 'favicon-blue-circle-48.png')
    create_transparent_favicon_with_blue_circle(32, 'favicon-blue-circle-32.png')
    create_transparent_favicon_with_blue_circle(16, 'favicon-blue-circle-16.png')
    
    print("\n✅ すべての透過背景ファビコンが生成されました！")
    print("\n📁 生成されたファイル:")
    print("   - 完全透過: favicon-transparent*.png")
    print("   - 青い円背景: favicon-blue-circle*.png")
