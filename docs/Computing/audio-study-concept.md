# Audio Study Concept

_Thực ra cái chương này liên quan nhiều đến DSP hơn là "audio concepts"_

## Faust

Faust (Functional Audio Stream) là một ngôn ngữ lập trình hàm dành cho tổng hợp âm thanh và xử lý âm thanh, tập trung mạnh vào thiết kế bộ tổng hợp âm thanh, nhạc cụ, hiệu ứng âm thanh, v.v. Faust hướng đến các ứng dụng xử lý tín hiệu hiệu suất cao và các plugin âm thanh cho nhiều nền tảng và tiêu chuẩn khác nhau. Nó được sử dụng trên sân khấu cho các buổi hòa nhạc và sản xuất nghệ thuật, trong giáo dục và nghiên cứu, trong các dự án mã nguồn mở cũng như trong các ứng dụng thương mại.

- Trang chủ: <https://faustdoc.grame.fr/>
- Github: <https://github.com/grame-cncm/faust>
- Khóa học trực tuyến: <https://ccrma.stanford.edu/~rmichon/faustWorkshops/course2015/#gainController>
- Faust Tutorials: <https://ccrma.stanford.edu/~rmichon/faustTutorials>
- Faust IDE: <https://faustide.grame.fr/>
	```text title="Code test"
	import("stdfaust.lib");
	import("music.lib");
	import("filter.lib");

	gainController = *(gain : smooth(tau2pole(interpTime)))
	with{
		gain = hslider("gain",0.5,0,10,0.1);
		interpTime = hslider("Interpolation Time (s)",0.5,0,10,0.1);
	};

	ringMod = *(1-depth*(osc(freq_ring)*0.5+0.5))
	with{
		freq_ring = hslider("frequency",5,0.1,1000,0.01) : smooth(0.999);
		depth = hslider("depth",0,0,1,0.01) : smooth(0.999);
	};

	import("music.lib");
	mySine(n) = osc(freq)
	with{
		freq = hslider("freq %n",440,50,1000,0.01);
	};

	process = ba.pulsen(1, 10000) : pm.djembe(60, 0.3, 0.4, 1) : ringMod : gainController <: dm.freeverb_demo;
	// process = par(i,4,mySine(i)) :> ringMod : gainController;
	```

## CCRMA Home Page

Trang này hướng dẫn khá là nhiều về các loại âm thanh và các khái niệm liên quan đến **DSP**.

- CCRMA Home Page: <https://ccrma.stanford.edu/%7Ejos/Welcome.html>
- CCRMA Stanford Edu: <https://ccrma.stanford.edu/>

## DSPi

Biến Ras Pico trở thành một phần cứng DSP tiêu chuẩn. Tôi không biết đấu dây thế nên nó khá là vấn đề.

- Github: <https://github.com/WeebLabs/DSPi>
- Review: <https://www.audiosciencereview.com/forum/index.php?threads/introducing-dspi-a-powerful-user-friendly-and-open-source-dsp-for-less-than-a-cup-of-coffee.69343/>

## OpenDSP

OpenDSP là một hệ điều hành thời gian thực (Realtime Operational System) được thiết kế ưu tiên cho việc xử lý tín hiệu số âm thanh và video trên các thiết bị nhúng như Raspberry Pi.

- Github: <https://github.com/midilab/opendsp>

## Open Hardware DSP Platform

Nền tảng phần cứng mở cho việc xử lý DSP. Trang này tập trung hướng đến xây dựng mạch PCB phần cứng.

- Introduce: <https://ohdsp.weebly.com/>

!!! quote "Không liên quan đến audio"
	- [Learning Curve](https://en.wikipedia.org/wiki/Learning_curve)
	- [Forgetting Curve](https://en.wikipedia.org/wiki/Forgetting_curve)