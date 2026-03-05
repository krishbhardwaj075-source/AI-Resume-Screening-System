const input = document.getElementById("resumeInput");
const plusIcon = document.getElementById("plusicon");
const fileIcon = document.getElementById("pdficon");
const fileName = document.getElementById("filename");

function updateUploadUI() {
    if (!input || !plusIcon || !fileIcon || !fileName) return;

    if (input.files && input.files.length > 0) {
        fileName.textContent = input.files[0].name;
        plusIcon.style.display = "none";
        fileIcon.style.display = "inline";
    } else {
        fileName.textContent = "No file selected";
        plusIcon.style.display = "inline";
        fileIcon.style.display = "none";
    }
}

if (input && plusIcon && fileIcon && fileName) {
    updateUploadUI();
    input.addEventListener("change", updateUploadUI);
}
