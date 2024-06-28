import numpy as np ,cv2
from common.histogram import draw_histo
# 최대 값이랑 최소값을 확인하고 그 위치를 좌우로 잡아당겨 고른 명암 분포를 가진 히스토그램이 되게하는거
# 화질 개선효고하가 있음

def search_value_idx(hist, bias = 0):                   #값 있는 첫 계급 검색 함수
    for i in range(hist.shape[0]):
        idx = np.abs(bias - i)                          #검색위치 (처음 또는 마지막)
        if hist[idx] > 0: return idx                    #위치 반환
    return -1                                           # 대상없으면 반환




image = cv2.imread("images/j2.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

bsize, ranges = [64],[0,256]                                #계급 개수 및 화소 범위
hist = cv2.calcHist([image],[0],None,bsize,ranges)

bin_width = ranges[1]/bsize[0]                          #한계급 너비
low = search_value_idx(hist,0) * bin_width          #최저 화소값
high = search_value_idx(hist,bsize[0] -1 ) * bin_width  # 최고 화소값

idx = np.arange(0,256)                              # 룩업 인덱스(0~255) 생성
idx = (idx-low)/(high-low) * 256                    # 수식 적용하여 룩업 인덱스 완성
idx[0:int(low)] = 0                                 # 히스토그램 하위 부분
idx[int(high+1):] = 255                             # 히스토그램 상위 부분
dst = cv2.LUT(image,idx.astype('uint8')) #록업 테이블
## 록업 테이블 사용하지 안고 직접 구현
# dst = np.zeros(image.shape, dtype=image.dtype)
# for i in range(dst.shape[0]):
#       for j in range(dst.shape[1]):
#           dst[i,j] = idx[image[i,j]]



hist_dst = cv2.calcHist([dst],[0],None,bsize,ranges) # 결과 영상 히스토그램 재계산
hist_img = draw_histo(hist,(200,360))                               #원본 영상 히스토그램 그리기
hist_dst_img = draw_histo(hist_dst, (200,360))                      #결과영상 히스토그램 그리기

print("high_value", high)
print("low_value", low)
cv2.imshow("image", image);     cv2.imshow("hist_img", hist_img)
cv2.imshow("dst", dst)  ; cv2.imshow("hist_dst_img", hist_dst_img)
cv2.waitKey(0)