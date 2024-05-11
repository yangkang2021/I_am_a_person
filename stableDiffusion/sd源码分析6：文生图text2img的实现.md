# sd源码分析6：文生图text2img的实现
> modules/txt2img.py
> 
> modules/processing.py
> 
> modules/sd_samplers_kdiffusion.py
> 
> repositories/k-diffusion/k_diffusion/sampling.py

## 一. 调用流程
- submit的click：没有传递主模型参数，扩展模型如lora参数，插件controlnet参数等等
- wrap_gradio_gpu_call：基于线程锁的任务队列，能解决多人使用问题
- wrap_gradio_call：统计性能
- modules.txt2img.txt2img
- process_images：如果有脚本会先：modules.scripts.scripts_txt2img.run
- process_images_inner
- samples_ddim = p.sample(...)
  - create_sampler/KDiffusionSampler()
  - KDiffusionSampler的sample(...)
  - launch_sampling(...)
  - k_diffusion项目sample_euler_ancestral
  - CFGDenoiser.forward(...)//step次
- res = Processed(p, output_images,...)
```
txt2img_args = dict(
    fn=wrap_gradio_gpu_call(modules.txt2img.txt2img, extra_outputs=[None, '', '']),
    _js="submit",
    inputs=[
        dummy_component,
        txt2img_prompt,
        txt2img_negative_prompt,
        txt2img_prompt_styles,
        steps,
        sampler_index,
        restore_faces,
        tiling,
        batch_count,
        batch_size,
        cfg_scale,
        seed,
        subseed, subseed_strength, seed_resize_from_h, seed_resize_from_w, seed_checkbox,
        height,
        width,
        enable_hr,
        denoising_strength,
        hr_scale,
        hr_upscaler,
        hr_second_pass_steps,
        hr_resize_x,
        hr_resize_y,
        override_settings,
    ] + custom_inputs,

    outputs=[
        txt2img_gallery,
        generation_info,
        html_info,
        html_log,
    ],
    show_progress=False,
)

txt2img_prompt.submit(**txt2img_args)
submit.click(**txt2img_args)
```