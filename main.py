import time
import random
from tqdm import tqdm
import numpy as np

CODENAME = "trixie"
ARCH = "amd64"

DATABASE = {
    "Kernel": ["linux-image", "linux-headers", "linux-modules", "linux-kbuild"],
    "Library": ["libc6", "libssl3t64", "libstdc++6", "libgcc-s1", "libpam0g"],
    "System": ["base-files", "apt", "dpkg", "systemd", "udev"],
    "SharedObj": ["libc.so.6", "libm.so.6", "libpthread.so.0", "libdl.so.2"]
}

Global = True

def simular_proceso(package_name, version, modo="Downloading"):
    global Global
    if modo == "Downloading":
        total = np.random.randint(100, 10000)
        unit = "MB"
        speed_range = (8.0, 20.0)
    else:
        total = np.random.randint(1200, 3000)
        unit = "it"
        speed_range = (40.0, 85.0)

    desc = f"{modo:13} {package_name}_{version}_{ARCH}.deb"
    
    with tqdm(total=total, unit=unit, unit_scale=True, desc=desc, colour="white", leave=True, ascii="░▒█") as pbar:
        actual = 0
        while actual < total and Global:
            try:
                base_step = random.uniform(*speed_range)
                jitter = random.uniform(-0.1, 0.1) * base_step
                paso = base_step + jitter
                
                if actual + paso > total:
                    paso = total - actual
                
                time.sleep(0.04)
                pbar.update(paso)
                actual += paso
            except (KeyboardInterrupt, EOFError):
                Global = False
                break

if __name__ == "__main__":
    print(f"--- Updating Repositories ({CODENAME}) ---")
    time.sleep(1)
    
    try:
        while Global:
            category = random.choice(list(DATABASE.keys()))
            package = random.choice(DATABASE[category])

            v_main = np.random.randint(1, 7)
            v_sub = np.random.randint(0, 25)
            version = f"{v_main}.{v_sub}.0-release"

            simular_proceso(package, version, modo="Downloading")
            if not Global: break
            time.sleep(0.2)
            simular_proceso(package, version, modo="Unpacking")
            
            if Global:
                print(f"Setting up {package} ({version}) [{ARCH}] ... ", end="", flush=True)
                time.sleep(np.random.randint(5, 20)) 
                print("done.")
                time.sleep(0.3)

    except KeyboardInterrupt:
        print(f"\n\n⚠️ Update aborted. Resources for '{CODENAME}' remain unchanged.")
