# This file is part of the pdfsp project
# Copyright (C) 2025 Sermet Pekin
#
# This source code is free software; you can redistribute it and/or
# modify it under the terms of the European Union Public License
# (EUPL), Version 1.2, as published by the European Commission.
#
# You should have received a copy of the EUPL version 1.2 along with this
# program. If not, you can obtain it at:
# <https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12>.
#
# This source code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# European Union Public License for more details.
#
# Alternatively, if agreed upon, you may use this code under any later
# version of the EUPL published by the European Commission.
from pdfsp import extract_tables, Options




def test_full(capsys):

    from pdfsp import extract_tables

    with capsys.disabled():
        source_folder = "."
        output_folder = "output_t"
        options = Options(source_folder=source_folder, output_folder=output_folder)

        extract_tables(options)
def test_full_combine(capsys):

    from pdfsp import extract_tables

    with capsys.disabled():
        source_folder = "."
        output_folder = "output_t"
        options = Options(source_folder=source_folder, output_folder=output_folder , combine=True)

        extract_tables(options)