<!-- <template>
  <div>
    <div class="nav" style="
          background-color: none;
          border-bottom: solid 0px #9a2b2e;
          box-shadow: 0px 3px 3px rgba(0, 0, 0, 0);
        " id="nav">
      <div class="logo">
        <img style="width: 100%" src="../assets/brickslogo.png" alt="" />
      </div>
      <div class="nav_button">
        <button class="button try" type="button" onclick="location.href='https://www.nccu.edu.tw/app/home.php'">
          試用
        </button>
        <button class="button login" type="button" onclick="location.href='./Login'">
          登入
        </button>
        <button class="button" type="button" onclick="location.href='./Register'">
          註冊
        </button>
      </div>
    </div>
    <div class="main-vis-slogan">
      <div class="hpp">
        <div class="hpp_top">
          <div class="slogan slo1">一磚一磚 &nbsp;建造</div>
          <div class="slogan slo2">你的專案</div>
          <div class="slogan slo3">為大學生設計的專案管理工具</div>
        </div>
        <button class="button start" type="button" onclick="location.href='https://www.nccu.edu.tw/app/home.php'">
          立即試用
        </button>
      </div>
    </div>
    <div class="bricks_bg">
      <div class="show show-dark">
        <div class="text">
          最方便的會議紀錄
          <br />
          <div class="pros">
            <ul>
              <li># 利用<b>Hashtag</b>標籤，快速搜尋過往內容</li>
              <br />
              <li># 建立自訂的<b>範本</b>， 不再需要每次重開</li>
              <br />
              <li># <b>封存</b>先前的紀錄，避免不慎更動</li>
            </ul>
          </div>
          <button class="button try" type="button" onclick="location.href='https://www.nccu.edu.tw/app/home.php'">
            開始試用
          </button>
        </div>
        <div class="pic"><img src="../assets/sample.png" alt="" /></div>
      </div>
      <div class="show show-grey">
        <div class="pic2"><img src="../assets/sample.png" alt="" /></div>
        <div class="text">
          繪製組織架構圖
          <br />
          <div class="pros">
            <ul>
              <li># <b>圖像化</b>的架構，組織層級一目瞭然</li>
              <br />
              <li># 依照層級賦予<b>權限</b></li>
              <br />
              <li># 可<b>隨時更改</b>，應付各種人員流動</li>
            </ul>
          </div>
        </div>
      </div>
      <div class="show show-white">
        <div class="text">
          IG式提案
          <br />
          <div class="pros">
            <ul>
              <li># <b>隨時隨地</b>向眾人發表提案</li>
              <br />
              <li># 投票、抽籤等<b>多功能</b>彙總</li>
              <br />
              <li># <b>大學生熟悉</b>的操作介面</li>
            </ul>
          </div>
        </div>
        <div class="pic"><img src="../assets/sample.png" alt="" /></div>
      </div>
    </div>
  </div>
</template>

<script>
window.onscroll = function () {
  if (document.documentElement.scrollTop >= 990) {
    nav.style.backgroundColor = "white";
    // nav.style.borderBottom = "solid 1px black"
    nav.style.boxShadow = "0px 3px 3px rgba(0,0,0,0.3)";
  } else if (document.documentElement.scrollTop < 990) {
    nav.style.backgroundColor = "transparent";
    // nav.style.borderBottom = "solid 0px black"
    nav.style.boxShadow = "0px 3px 3px rgba(0,0,0,0)";
  }
};
</script>

<style scoped>
* {
  position: relative;
  font-family: "Noto Sans TC", sans-serif;
  margin: 0;
}

body {
  margin: 0;
  position: static;
  /* 高度占整個螢幕，body要先設height: 100% */
  height: 100%;
}

.nav {
  z-index: 999;
  position: fixed;
  display: block;
  /* background-color: #9A2B2E; */
  width: 1920px;
  height: 98px;
  /* border-bottom: solid 1px black; */
}


.nav .logo {
  display: inline-block;
  position: absolute;
  /* top: 3px; */
  left: 7.3%;
  height: 100%;
  width: 15.417vw;

  /* padding: 0px 30px; */
  /* margin: 2px 0; */
}

.nav_button {
  width: 20vw;
  height: 100%;
  position: absolute;
  right: 9.7917%;
}

.nav .button {
  width: 30%;
  height: 44.9%;
  position: absolute;
  font-size: 2.2vh;
  border: solid 1px #363b3e;
  background-color: #f3f7f7;
  color: #363b3e;
  border-radius: 25px;
  right: 0;
  cursor: pointer;
  top: 50%;
  transform: translate(0, -50%);
}

.nav .login {
  right: 35.0725%;
  border: solid 1px #9a2b2e;
  color: #f3f7f7;
  background-color: #9a2b2e;
}

.nav .try {
  left: 0%;
}

.hpp button {
  cursor: pointer;
}

.main-vis-slogan {
  position: relative;
  margin: 0;
  padding: 0;
  width: 100%;
  /* 高度占整個螢幕 */
  height: 100vh;
  background: #f3f7f7;
}

.hpp {
  position: relative;
  background-image: url("../assets/hpp1.jpg");
  width: 100%;
  height: 100vh;
  background-size: cover;
}

.hpp_top {
  background-color: #ffffff;
  width: 100%;
  height: 100vh;
  opacity: 0.8;
}

.slogan {
  position: absolute;
  z-index: 99;
  left: 50%;
  top: 33%;
  color: black;
  transform: translate(-50%, -50%);
}

.slogan.slo1 {
  font-size: 72px;
  font-weight: bold;
}

.slogan.slo2 {
  font-size: 72px;
  top: 45%;
  font-weight: bold;
}

.slogan.slo3 {
  font-size: 23px;
  top: 58%;
  /* font-weight: bold; */
}

.button.start {
  z-index: 998;
  position: absolute;
  left: 50%;
  top: 68%;
  transform: translate(-50%, -50%);
  font-size: 15px;
  border: solid 1px #9a2b2e;
  background-color: #9a2b2e;
  color: #f3f7f7;
  padding: 8px 30px;
  border-radius: 25px;
}

.bricks_bg {
  z-index: 10;
  background-image: url("../assets/bricks_bg.svg");
  width: 100%;
  height: 100%;
  background-size: cover;
}

.show.show-dark {
  width: 100%;
  height: 95vh;
  /* background-color: #fcfcfc; */
}

.show.show-dark .text {
  position: absolute;
  left: 12%;
  top: 30%;
  /* transform: translate(0%, -50%); */
  font-size: 45px;
  font-weight: bold;
}

.show.show-dark .pros {
  margin-top: 12%;
  font-size: 17px;
  font-weight: normal;
  /* top: 50%; */
}

ul {
  list-style-type: none;
}

.show.show-dark .button.try {
  font-size: 14px;
  border: solid 1px #9a2b2e;
  /* background-color: #Fcfcfc; */
  display: inline-block;
  color: #9a2b2e;
  padding: 5px 30px;
  border-radius: 25px;
  /* margin: 8px 0; */
  font-weight: bold;
  cursor: pointer;
}

.show.show-grey {
  width: 100%;
  height: 95vh;
  color: #252525;
  /* background-color: #fcfcfc; */
}

.show.show-grey .text {
  position: absolute;
  left: 62%;
  top: 30%;
  /* transform: translate(0%, -50%); */
  font-size: 45px;
  font-weight: bold;
}

.show.show-grey .pros {
  margin-top: 12%;
  font-size: 17px;
  font-weight: normal;
  /* top: 50%; */
}

.show.show-white {
  width: 100%;
  height: 95vh;
  color: #363b3e;
  /* background-color: #fcfcfc; */
}

.show.show-white .text {
  position: absolute;
  left: 12%;
  top: 30%;
  /* transform: translate(0%, -50%); */
  font-size: 45px;
  font-weight: bold;
}

.show.show-white .pros {
  margin-top: 12%;
  font-size: 17px;
  font-weight: normal;
  /* top: 50%; */
}

.pic {
  position: absolute;
  left: 50%;
  top: 50%;
  display: inline-block;
  width: 593px;
  height: 551px;
  transform: translate(0%, -50%);
}

.pic2 {
  position: absolute;
  right: 50%;
  top: 50%;
  display: inline-block;
  width: 540px;
  transform: translate(0%, -50%);
}
</style> -->
