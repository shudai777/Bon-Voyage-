#!/usr/bin/env python3
"""
Bon Voyage ウェブサイト用QRコード生成スクリプト
"""

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, CircleModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

def create_basic_qr():
    """基本的なQRコード（シンプル・黒）"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 高い誤り訂正
        box_size=10,
        border=4,
    )
    
    # URLを設定
    qr.add_data('https://shudai777.github.io/Bon-Voyage-/')
    qr.make(fit=True)
    
    # 画像を作成
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qrcode_basic.png')
    print("✅ 基本QRコード作成完了: qrcode_basic.png")

def create_styled_qr():
    """スタイリッシュなQRコード（丸みあり・ブランドカラー）"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data('https://shudai777.github.io/Bon-Voyage-/')
    qr.make(fit=True)
    
    # スタイリッシュな画像を作成（角丸・ブルー系）
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),  # 角丸スタイル
        color_mask=SolidFillColorMask(
            front_color=(26, 115, 232),  # ブランドカラー（ブルー）
            back_color=(255, 255, 255)   # 白背景
        )
    )
    img.save('qrcode_styled.png')
    print("✅ スタイリッシュQRコード作成完了: qrcode_styled.png")

def create_circle_qr():
    """サークル型QRコード"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data('https://shudai777.github.io/Bon-Voyage-/')
    qr.make(fit=True)
    
    # サークル型
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=CircleModuleDrawer(),
        color_mask=SolidFillColorMask(
            front_color=(0, 212, 255),  # アクセントカラー（水色）
            back_color=(255, 255, 255)
        )
    )
    img.save('qrcode_circle.png')
    print("✅ サークル型QRコード作成完了: qrcode_circle.png")

def create_high_res_qr():
    """高解像度QRコード（印刷用）"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,  # 大きめのボックスサイズ
        border=5,
    )
    
    qr.add_data('https://shudai777.github.io/Bon-Voyage-/')
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qrcode_highres.png')
    print("✅ 高解像度QRコード作成完了: qrcode_highres.png")

if __name__ == "__main__":
    print("🎨 Bon Voyage QRコード生成中...\n")
    
    # 各種QRコードを生成
    create_basic_qr()
    create_styled_qr()
    create_circle_qr()
    create_high_res_qr()
    
    print("\n✨ すべてのQRコードが生成されました！")
    print("\n📂 生成されたファイル:")
    print("  - qrcode_basic.png    : 基本的なQRコード（黒・シンプル）")
    print("  - qrcode_styled.png   : スタイリッシュQRコード（角丸・ブルー）")
    print("  - qrcode_circle.png   : サークル型QRコード（水色）")
    print("  - qrcode_highres.png  : 高解像度QRコード（印刷用）")
