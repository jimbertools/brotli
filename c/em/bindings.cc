#include <emscripten/bind.h>
#include <iostream>
#include "brotli/decode.h"
using namespace emscripten;


uint32_t BrotliDecoderVersion();

float lerp(float a, float b, float t) {
    std::cout << " hey " << std::endl << std::flush;
    return (1 - t) * a + t * b;
}

EMSCRIPTEN_BINDINGS(my_module) {
    function("lerp", &lerp);
    function("version", &BrotliDecoderVersion);
}
