#include <thread>
#include <mach-o/dyld.h>

int main()
{
    std::this_thread::sleep_for(std::chrono::seconds(20));
    uintptr_t offset = 0x1001b966c;
    typedef int (*printdef)(int, const char*, ...);
    auto printfunction = reinterpret_cast<printdef>(_dyld_get_image_vmaddr_slide(0) + (uintptr_t)offset);

    auto delayprint = [&](int type, const char* message, std::chrono::milliseconds delay) {
        std::this_thread::sleep_for(delay);
        printfunction(type, message);
    };

    delayprint(0, "Print Execution Successful", std::chrono::milliseconds(200));
    delayprint(0, "2024, Exploit", std::chrono::milliseconds(200));
    delayprint(2, "Expected Bugs, Crashes Report Logs to discord server.", std::chrono::milliseconds(200));
    delayprint(0, "Injection Soon 🔜", std::chrono::milliseconds(200));
    delayprint(2, "MacOS, Windows Support Soon", std::chrono::milliseconds(200));
    delayprint(0, "Injection 50 %", std::chrono::milliseconds(200));

    return 0;
}

__attribute__((constructor)) void entry()
{
    printf("[ Custom printsploit dylib injected ]\n");
    std::thread(main).detach();
}
