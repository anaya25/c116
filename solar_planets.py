import cv2

img = cv2.imread(“solar-system.jpg”)

cv2.imshow(“output”,img)

cv2.waitkey(0)

cv2.putText(
    img,
    "Sun",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "MERCURY",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "VENUS",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "EARTH",
    (30,710),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "MARS",
    (40,320),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "JUPITER",
    (50,330),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "SATURN",
    (60,340),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "URANUS",
    (70,350),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "NEPTUNE",
    (80,360),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.imwrite(“Solar_systemwithname.jpg”,img)