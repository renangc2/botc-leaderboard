document.addEventListener('DOMContentLoaded', () => {
    const bgmAudio = document.getElementById('bgm-audio');
    const bgmToggle = document.getElementById('bgm-toggle');

    if (!bgmAudio || !bgmToggle) return;

    // 获取上一次存储的播放状态，默认是 false
    const isPlaying = localStorage.getItem('botc_bgm_playing') === 'true';

    // 根据历史状态初始化播放
    if (isPlaying) {
        // 由于浏览器的自动播放策略，必须捕获异常，如果被拦截则停止旋转动画
        bgmAudio.play().then(() => {
            bgmToggle.classList.add('playing');
        }).catch((err) => {
            console.log("浏览器拦截了自动播放:", err);
            localStorage.setItem('botc_bgm_playing', 'false');
            bgmToggle.classList.remove('playing');
        });
    }

    // 绑定点击开关事件
    bgmToggle.addEventListener('click', () => {
        if (bgmAudio.paused) {
            bgmAudio.play();
            bgmToggle.classList.add('playing');
            localStorage.setItem('botc_bgm_playing', 'true');
        } else {
            bgmAudio.pause();
            bgmToggle.classList.remove('playing');
            localStorage.setItem('botc_bgm_playing', 'false');
        }
    });
});
