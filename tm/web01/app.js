let model, webcam, labelContainer, maxPredictions;

// モデルのロードとカメラのセットアップ
async function init() {
    const modelURL = 'https://teachablemachine.withgoogle.com/models/VB0KENdaR/model.json';
    const metadataURL = 'https://teachablemachine.withgoogle.com/models/VB0KENdaR/metadata.json';

    model = await tmImage.load(modelURL, metadataURL);
    maxPredictions = model.getTotalClasses();

    const webcamElement = document.getElementById('webcam');
    webcam = new tmImage.Webcam(640, 480, true); // 幅、高さ、フリップを指定
    await webcam.setup(); // カメラの設定
    await webcam.play();
    window.requestAnimationFrame(loop);

    webcamElement.appendChild(webcam.canvas);
    labelContainer = document.getElementById('prediction');
}

// リアルタイムで画像を分類するループ関数
async function loop() {
    webcam.update(); // ビデオフレームを更新
    await predict();
    window.requestAnimationFrame(loop); // 次のフレームで再度実行
}

// 画像を分類する関数
async function predict() {
    const prediction = await model.predict(webcam.canvas);
    prediction.sort((a, b) => b.probability - a.probability);

    labelContainer.innerHTML = `予測: ${prediction[0].className} (${(prediction[0].probability * 100).toFixed(2)}%)`;
}

// ページが読み込まれたときにモデルとカメラを初期化
window.onload = init;
