<template>
    <div>
        <div class="nav" v-if="scroll" style="background-color: transparent;">
            <a href="./homepage_2">
                <img src="../assets/brickslogo.svg" alt="">
            </a>
            <div class="tribtn">
                <div class="btn">試用</div>
                <a href="./login_2" class="btn nav_login_btn"
                    style="background-color: #b82c30; border-color: #b82c30; color: #ffffff;">登入</a>
                <a href="./register_2" class="btn" style="margin-right: 0px;">註冊</a>
            </div>
        </div>
        <div class="nav_scroll" v-else style="background-color: white;">
            <a href="./homepage_2">
                <img src="../assets/brickslogo.svg" alt="">
            </a>
            <div class="tribtn">
                <div class="btn">試用</div>
                <a href="./login_2" class="btn nav_login_btn"
                    style="background-color: #b82c30; border-color: #b82c30; color: #ffffff;">登入</a>
                <a href="./register_2" class="btn" style="margin-right: 0px;">註冊</a>
            </div>
        </div>
        <div class="first_bg">
            <div class="slogan">
                <div class="first_line">
                    <p style="float: left;">一磚一磚</p>
                    <p style="float: right;">建<span style="letter-spacing: 0;">造</span></p>
                </div>
                <p class="second_line">你的專<span style="letter-spacing: 0;">案</span></p>
                <p class="third_line">為大學生設計的專案管理工<span style="letter-spacing: 0;">具</span></p>
                <a href="" class="try_now_first">立即試用</a>
            </div>
        </div>
        <div class="sec_body">
            <div class="card">
                <img src="../assets/screen_shot.png" alt="">
                <div class="text_area first_text_area">
                    <p class="line_one"># 輕鬆開會</p>
                    <p class="line_two">最方便的會議紀錄</p>
                    <p class="three_adv">
                        # 利用 Hashtag 標籤，快速搜尋過往內容<br>
                        # 建立自訂的範本，不再需要每次重開<br>
                        # 封存先前的紀錄，避免不慎更動
                    </p>
                </div>
                <a href="" class="mid_try_btn">立即試用</a>
            </div>
            <div class="card sec_card">
                <img src="../assets/screen_shot.png" alt="">
                <div class="text_area">
                    <p class="line_one"># 層級分明</p>
                    <p class="line_two">繪製組織架構圖</p>
                    <p class="three_adv">
                        # 圖像化的架構，組織層級一目瞭然<br>
                        # 依照層級賦予權限<br>
                        # 可隨時更改，應付各種人員流動
                    </p>
                </div>
            </div>
            <div class="card">
                <img src="../assets/screen_shot.png" alt="">
                <div class="text_area">
                    <p class="line_one"># 創意發想</p>
                    <p class="line_two">隨時隨地 IG 式提案</p>
                    <p class="three_adv">
                        # 隨時隨地向眾人發表提案<br>
                        # 類 IG 的操作介面<br>
                        # 投票、抽籤等多功能匯總
                    </p>
                </div>
            </div>
            <div class="last_text_area">
                <p class="end_first_line">
                    比 Google 文件更方便<br>
                    比 Notion 更直覺
                </p>
                <p class="end_sec_area">
                    周全不繁瑣的會議功能<br>
                    簡單易上手的操作介面<br>
                    現在就用 <span style="color:#b82c30">BRICKS</span> 完善你的專案！
                </p>
                <a href="" class="end_try_btn">立即試用</a>
            </div>
        </div>
        <div class="bottom">
            <a href="" class="privacy"># <span style="text-decoration: underline;">隱私權政策</span></a>
            <a href="" class="contact"># 聯絡我們 <span style="color: #b6aeae;">bricks@gmail.com</span></a>
            <div class="photo"># Photo by <a href="https://unsplash.com/@charlesdeluvio">charlesdeluvio</a> on Unsplash
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Homepage_2',
    data() {
        return {
            scroll: true,
        };
    },
    methods: {
        handleScroll() {
            var top = Math.floor(document.documentElement.scrollTop);
            // var screenHeight = window.innerHeight;
            // var threshold = screenHeight * 1; // 將螢幕高度乘上1，即為100%的高度


            if (top > 1015) {           //記得減掉navbar的高度  1080-65
                this.scroll = false;
            } else {
                this.scroll = true;
            }
        }
    },
    created() {

    },
    mounted() {
        window.addEventListener('scroll', this.handleScroll);
    }
}
</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
    font-family: 'Noto Sans TC';
}

.nav {
    width: 100vw;
    height: 65px;
    position: fixed;
    top: 0;
}

.nav_scroll {
    width: 100vw;
    height: 65px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    position: fixed;
    top: 0;
    z-index: 9;
}

.nav img {
    height: 32.06px;
    width: auto;
    position: absolute;
    top: 16.47px;
    left: 5.21%;
}

.nav_scroll img {
    height: 32.06px;
    width: auto;
    position: absolute;
    top: 16.47px;
    left: 5.21%;
}

.tribtn {
    width: 284px;
    height: 41px;
    position: absolute;
    top: 12px;
    right: 5.21%;
}

.btn {
    width: 76px;
    height: 39px;
    border: 1px solid #120405;
    background-color: transparent;
    border-radius: 10px;
    float: left;
    margin-right: 25px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 500;
    line-height: 39px;
    font-family: 'Noto Sans TC';
    text-align: center;
    letter-spacing: 1.25px;
    user-select: none;
    text-decoration: none;
    color: black;
}

.btn:hover {
    background-color: rgba(242, 238, 238, 1);
}

.nav_login_btn:hover {
    background-color: rgba(212, 128, 131, 1) !important;
}

.first_bg {
    background-image: url(../assets/homepage_bg.svg);
    width: 100%;
    height: 1080px;
    background-size: cover;
    margin-top: -65px;
    background-position: top;
}

.slogan {
    width: 880px;
    height: 368px;
    position: relative;
    left: 50%;
    transform: translate(-50%);
    top: 265px;
    font-family: 'Noto Sans TC';

}

.first_line {
    font-size: 47px;
    font-weight: 400;
    height: 56.4px;
    width: 444px;
    line-height: 56.4px;
    position: absolute;
    left: 50%;
    transform: translate(-50%);
    letter-spacing: 12px;
    top: 0px;
}

.second_line {
    font-size: 93px;
    font-weight: 700;
    height: 112px;
    width: 444px;
    line-height: 112px;
    position: absolute;
    left: 50%;
    transform: translate(-50%);
    letter-spacing: 24px;
    top: 68px;
}

.third_line {
    font-size: 33px;
    font-weight: 400;
    height: 40px;
    width: auto;
    line-height: 40px;
    position: absolute;
    left: 50%;
    transform: translate(-50%);
    letter-spacing: 0.25px;
    top: 200px;
}

.try_now_first {
    width: 272px;
    height: 48px;
    background-color: #b82c30;
    border-radius: 14px;
    position: absolute;
    bottom: 0px;
    left: 50%;
    transform: translate(-50%);
    text-decoration: none;
    font-size: 18px;
    font-weight: 500;
    color: white;
    line-height: 48px;
    text-align: center;
    letter-spacing: 4px;
}

.try_now_first:hover {
    background-color: #d48083;
}

.try_now_first:active {
    background-color: #932326;
}

.sec_body {
    width: 100vw;
    height: 3306px;
    background-image: url(../assets/bricks_bg.svg);
    background-size: cover;
}

.card {
    width: 77.5vw;
    height: 502px;
    position: relative;
    left: 50%;
    transform: translate(-50%);
    top: 250px;
    margin-bottom: 240px;
}

.sec_card img {
    float: left !important;
    left: 4% !important;
}

.card img {
    width: 60%;
    height: auto;
    aspect-ratio: 16/9;
    float: right;
    box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.4);
    position: relative;
    top: 50%;
    transform: translate(0, -50%);
    right: 4%;
}

.sec_card .text_area {
    right: 0 !important;
    float: right;
}

.text_area {
    width: auto;
    height: 232px;
    position: relative;
    top: 50%;
    transform: translate(0, -50%);
    left: 0;
}

.first_text_area {
    top: 68px;
    transform: none;
}

.line_one {
    height: 28px;
    line-height: 28px;
    color: #b6aeae;
    font-size: 23px;
    font-weight: 700;
}

.line_two {
    height: 56px;
    line-height: 56px;
    color: #252525;
    font-size: 47px;
    font-weight: 700;
}

.three_adv {
    position: relative;
    top: 48px;
    height: 100px;
    color: #252525;
    font-size: 23px;
    font-weight: 400;
}

.mid_try_btn {
    display: inline-block;
    color: #b82c30;
    height: 46px;
    width: 270px;
    border: 1px solid #b82c30;
    border-radius: 14px;
    background-color: white;
    position: absolute;
    top: 366px;
    left: 0;
    text-decoration: none;
    font-size: 18px;
    line-height: 46px;
    text-align: center;
    letter-spacing: 1.25px;
}

.mid_try_btn:hover {
    background-color: #f2eeee;
}

.mid_try_btn:active {
    background-color: #f1d5d6;
}

.last_text_area {
    width: 468px;
    height: 388px;
    position: relative;
    left: 50%;
    transform: translate(-50%);
    top: 240px;
}

.end_first_line {
    font-size: 47px;
    height: 56px;
    line-height: 56px;
    font-weight: 700;
    text-align: center;
}

.end_sec_area {
    font-size: 23px;
    font-weight: 400;
    text-align: center;
    position: relative;
    top: 104px;
}

.end_try_btn {
    display: inline-block;
    width: 272px;
    height: 48px;
    border-radius: 14px;
    background-color: #b82c30;
    color: white;
    letter-spacing: 4px;
    position: relative;
    top: 184px;
    left: 50%;
    transform: translate(-50%);
    text-decoration: none;
    line-height: 48px;
    font-size: 18px;
    text-align: center;
}

.end_try_btn:hover {
    background-color: #d48083;
}

.end_try_btn:active {
    background-color: #932326;
}

.bottom {
    width: 100vw;
    height: 65px;
    bottom: 0px;
    box-shadow: 0px -4px 8px rgba(0, 0, 0, 0.1);
    background-color: white;
    position: relative;
}

.privacy {
    width: 116px;
    height: 23px;
    font-size: 19px;
    font-family: 'Noto Sans TC';
    line-height: 23px;
    position: absolute;
    top: 50%;
    transform: translate(0, -50%);
    letter-spacing: 0.15px;
    cursor: pointer;
    color: #120406;
    text-decoration: none;
}

.contact {
    width: 271px;
    height: 23px;
    font-size: 19px;
    font-family: 'Noto Sans TC';
    line-height: 23px;
    position: absolute;
    top: 50%;
    transform: translate(0, -50%);
    letter-spacing: 0.15px;
    cursor: pointer;
    color: #120406;
    text-decoration: none;
}

.photo {
    width: 357px;
    height: 23px;
    font-size: 19px;
    font-family: 'Noto Sans TC';
    line-height: 23px;
    position: absolute;
    top: 50%;
    transform: translate(0, -50%);
    letter-spacing: 0.15px;
    color: #c7c2c2;
}

.photo a {
    color: #c7c2c2;
}

.privacy {
    left: 540px;
}

.contact {
    left: 688px;
}

.photo {
    right: 540px;
}
</style>