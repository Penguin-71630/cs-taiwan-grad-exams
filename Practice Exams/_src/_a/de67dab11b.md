<!-- src: devin -->
A. Memory-mapped I/O：device register 映射到記憶體位址，用一般 load/store 存取；I/O instruction：用專用 I/O 指令存取 device；Device polling：CPU 週期性讀 status register 檢查 device；Interrupt-driven：device 完成/需要服務時發 interrupt 通知 CPU\
B. Polling；遊戲迴圈每 frame 本來就要讀取控制器狀態，資料量小、頻率固定，polling 簡單且延遲可預期 [?] 亦有答 interrupt-driven 者\
C. Overheat > Reboot > Mouse controller [?] Reboot 與 Overheat 先後各書不一
