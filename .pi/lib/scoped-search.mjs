// A workflow guard for common literal whole-filesystem searches, not a shell sandbox.
export function isWholeFilesystemSearch(command) {
  if (typeof command !== "string") return false;
  const rootFind = /(?:^|[\s;&|()])(?:\/usr\/bin\/)?find\s+(?:-[HLP]\s+)*(?:\/|"\/"|'\/')(?=\s|$)/;
  const rootRg = /(?:^|[\s;&|()])(?:\/[^\s]+\/)?rg\s+[^;|\n]*\s(?:\/|"\/"|'\/')(?=\s|[;&|]|$)/;
  const rootGrep = /(?:^|[\s;&|()])(?:\/usr\/bin\/)?grep\s+(?=[^;|\n]*(?:--recursive|-[A-Za-z]*[rR]))[^;|\n]*\s(?:\/|"\/"|'\/')(?=\s|[;&|]|$)/;
  return rootFind.test(command) || rootRg.test(command) || rootGrep.test(command);
}
