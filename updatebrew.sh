#!/bin/bash

echo "Starting Homebrew update..."

# Ejecutar 'brew update' y capturar la salida
update_output=$(brew update)

# Verificar si la salida contiene "Already up-to-date."
if echo "$update_output" | grep -q "Already up-to-date."; then
    echo "Your Homebrew is already up-to-date. No updates available."
else
    echo "Updates available. Proceeding with the upgrade and cleanup process."

    echo "Running: brew upgrade"
    brew upgrade
    echo "Package upgrade completed."

    echo "Running: brew cleanup"
    brew cleanup
    echo "Cleanup completed."

    echo "Running: brew autoremove"
    brew autoremove
    echo "Auto-removal of unneeded packages completed."
fi

echo "All Homebrew processes have finished."

