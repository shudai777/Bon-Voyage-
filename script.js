// ===========================
// モバイルメニュートグル
// ===========================
const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const navMenu = document.querySelector('.nav-menu');

if (mobileMenuToggle && navMenu) {
    mobileMenuToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        mobileMenuToggle.classList.toggle('active');
    });

    // メニュー項目をクリックしたらメニューを閉じる
    const navLinks = document.querySelectorAll('.nav-menu a');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            mobileMenuToggle.classList.remove('active');
        });
    });

    // メニュー外をクリックしたら閉じる
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.nav-wrapper') && navMenu.classList.contains('active')) {
            navMenu.classList.remove('active');
            mobileMenuToggle.classList.remove('active');
        }
    });
}

// ===========================
// スクロール時のヘッダー背景変更
// ===========================
const header = document.querySelector('.header');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 100) {
        header.style.background = 'rgba(10, 14, 39, 0.98)';
        header.style.boxShadow = '0 2px 30px rgba(0, 0, 0, 0.5)';
    } else {
        header.style.background = 'rgba(10, 14, 39, 0.95)';
        header.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.3)';
    }
    
    lastScroll = currentScroll;
});

// ===========================
// スムーススクロール（古いブラウザ対応）
// ===========================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            const headerHeight = document.querySelector('.header').offsetHeight;
            const targetPosition = targetElement.offsetTop - headerHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// ===========================
// フォーム送信処理（Formspree対応）
// ===========================
const contactForm = document.getElementById('contactForm');

if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // 送信ボタンを無効化
        const submitButton = contactForm.querySelector('button[type="submit"]');
        const originalText = submitButton.textContent;
        submitButton.textContent = '送信中...';
        submitButton.disabled = true;
        
        // FormspreeのURLが設定されているか確認
        const formAction = contactForm.getAttribute('action');
        
        if (!formAction || formAction.includes('YOUR_FORM_ID')) {
            // Formspreeが未設定の場合はデモモード
            console.log('フォームデータ（デモモード）:', Object.fromEntries(new FormData(contactForm)));
            showNotification('⚠️ フォームは未設定です。Formspree IDを設定してください。', 'warning');
            submitButton.textContent = originalText;
            submitButton.disabled = false;
            return;
        }
        
        try {
            // Formspreeにデータを送信
            const response = await fetch(formAction, {
                method: 'POST',
                body: new FormData(contactForm),
                headers: {
                    'Accept': 'application/json'
                }
            });
            
            if (response.ok) {
                // 送信成功
                showNotification('お問い合わせを受け付けました。1営業日以内にご連絡いたします。', 'success');
                contactForm.reset();
            } else {
                // エラー
                throw new Error('送信に失敗しました');
            }
        } catch (error) {
            showNotification('送信に失敗しました。直接メールでご連絡ください。', 'error');
            console.error('フォーム送信エラー:', error);
        } finally {
            // ボタンを元に戻す
            submitButton.textContent = originalText;
            submitButton.disabled = false;
        }
    });
}

// ===========================
// 通知メッセージ表示
// ===========================
function showNotification(message, type = 'success') {
    // 既存の通知があれば削除
    const existingNotification = document.querySelector('.notification');
    if (existingNotification) {
        existingNotification.remove();
    }
    
    // 通知要素を作成
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // タイプに応じた背景色
    const colors = {
        'success': '#10b981',
        'error': '#ef4444',
        'warning': '#f59e0b'
    };
    
    // スタイルを設定
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: ${colors[type] || colors.success};
        color: white;
        padding: 1.5rem 2rem;
        border-radius: 10px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
        z-index: 10000;
        animation: slideInRight 0.3s ease;
        max-width: 400px;
        font-weight: 600;
    `;
    
    document.body.appendChild(notification);
    
    // 5秒後に自動的に削除
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 5000);
}

// 通知のアニメーション用CSS（動的に追加）
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// ===========================
// スクロールアニメーション（Intersection Observer）
// ===========================
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeInUp 0.8s ease forwards';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// アニメーション対象要素を監視
const animateElements = document.querySelectorAll(`
    .service-card,
    .case-card,
    .portfolio-item,
    .pricing-card,
    .credential-card
`);

animateElements.forEach(el => {
    el.style.opacity = '0';
    observer.observe(el);
});

// ===========================
// ページ読み込み時の処理
// ===========================
window.addEventListener('load', () => {
    // ヒーローセクションのアニメーション
    const heroContent = document.querySelector('.hero-content');
    if (heroContent) {
        heroContent.style.animation = 'fadeInUp 1s ease forwards';
    }
    
    // スクロールインジケーターのアニメーション
    const scrollIndicator = document.querySelector('.scroll-indicator');
    if (scrollIndicator) {
        scrollIndicator.style.animation = 'bounce 2s infinite';
    }
});

// ===========================
// 動画の遅延読み込み（パフォーマンス向上）
// ===========================
const videoObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const iframe = entry.target;
            const src = iframe.getAttribute('data-src');
            if (src) {
                iframe.setAttribute('src', src);
                iframe.removeAttribute('data-src');
            }
            videoObserver.unobserve(iframe);
        }
    });
}, {
    rootMargin: '200px'
});

// Vimeo iframeの遅延読み込み設定
// 注意: 実際に使用する場合は、HTMLのiframeのsrcをdata-srcに変更してください
document.querySelectorAll('.video-wrapper iframe').forEach(iframe => {
    videoObserver.observe(iframe);
});

// ===========================
// ユーティリティ関数
// ===========================

// スムーズスクロールユーティリティ
function smoothScrollTo(targetPosition, duration = 1000) {
    const startPosition = window.pageYOffset;
    const distance = targetPosition - startPosition;
    let startTime = null;
    
    function animation(currentTime) {
        if (startTime === null) startTime = currentTime;
        const timeElapsed = currentTime - startTime;
        const run = ease(timeElapsed, startPosition, distance, duration);
        window.scrollTo(0, run);
        if (timeElapsed < duration) requestAnimationFrame(animation);
    }
    
    function ease(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return c / 2 * t * t + b;
        t--;
        return -c / 2 * (t * (t - 2) - 1) + b;
    }
    
    requestAnimationFrame(animation);
}

// デバウンス関数（スクロールイベント最適化用）
function debounce(func, wait = 20, immediate = true) {
    let timeout;
    return function() {
        const context = this, args = arguments;
        const later = function() {
            timeout = null;
            if (!immediate) func.apply(context, args);
        };
        const callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
    };
}

// ===========================
// 開発用: ログ出力
// ===========================
console.log('%c🚁 Bon Voyage Website Loaded', 'font-size: 20px; color: #1a73e8; font-weight: bold;');
console.log('%cマイクロドローン室内撮影専門サービス', 'font-size: 14px; color: #00d4ff;');
console.log('お問い合わせはフォームからお願いいたします。');
