#include <thread>

std::this_thread::sleep_for(std::chrono::seconds(20));
    typedef int (*printdef)(int, const char*, ...);
    auto printfunction = reinterpret_cast<printdef>(_dyld_get_image_vmaddr_slide(0) + (uintptr_t)offset);
