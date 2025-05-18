window.onload = function () {
   const video = document.getElementById("introVideo");
   const audio = document.getElementById("introAudio");
   const introContent = document.getElementById("introContent");

   video.play();

   audio.play().catch(() => {
      const enableAudio = () => {
         audio.play().catch(() => {});
         document.removeEventListener("click", enableAudio);
      };

      document.addEventListener("click", enableAudio);
   });

   setTimeout(() => {
      introContent.classList.add("show");
   }, 29500);
};

function startGame() {
    window.location.href = "/game";
}